console.log("User Registration JS Loaded");

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

$.ajaxSetup({
    headers: { "X-CSRFToken": csrftoken }
});




$("#Continue_with").click(function (e) {
    e.preventDefault();

    console.log("Continue button clicked");

    const selectedType = $("#user_registration_type").val();
    console.log("selectedType:", selectedType);

    const termsAccepted = $("#termsCheck").is(":checked");

    if (!selectedType) {
        toastr.error("Please select a registration type before continuing.");
        return;
    }
    if (!termsAccepted) {
        toastr.error("Please accept the Terms and Conditions.");
        return;
    }

    const formData = new FormData();
    formData.append("csrfmiddlewaretoken", csrftoken);
    formData.append("user_registration_type", selectedType.toLowerCase());
    formData.append("terms_and_conditions", termsAccepted ? "true" : "false");


    $.ajax({
        type: "POST",
        url: "/user_registration",
        data: formData,
        cache: false,
        contentType: false,
        processData: false,
        success: function (response) {
            console.log("Server response:", response);
            toastr.success(response.message);

            const userType = (response.user_type || response.user_registration_type || "").toLowerCase();
            if (!userType) {
                toastr.error("User type missing in response.");
                console.warn("Response did not include user_type key:", response);
                return;
            }

            localStorage.setItem("user_registration_type", userType);
            console.log("Saved user_registration_type:", userType);

            console.log("localStorage now:", localStorage.getItem("user_registration_type"));

            console.log("Redirect intentionally disabled for testing. Full response:", response);
            setTimeout(() => {
                if (userType === "arbitrator") {
                    window.location.href = "/arbitrator";
                } else if (userType === "mediator") {
                    window.location.href = "/mediator";
                } else if (userType === "bank_individual") {
                    window.location.href = "/personal_information";
                } else {
                    toastr.error("Unknown user type. Please contact support.");
                }
            }, 300);

        },
        error: function (xhr) {
            console.error("Error:", xhr.status, xhr.responseText);
            toastr.error(xhr.responseJSON?.error || "Something went wrong during registration.");
        },
    });
});


$(document).ready(function () {
    const savedType = localStorage.getItem("user_registration_type");

    if (savedType) {
        $("#user_registration_type").val(savedType);
        console.log("Loaded user_registration_type from localStorage:", savedType);
    } else {
        console.warn("No user_registration_type found in localStorage.");
        toastr.warning("Please complete registration first.");
       
    }
});

$(document).ready(function () {
    $("#arbitrator_registration_form").on("submit", function (e) {
        e.preventDefault();

        console.log("Arbitrator form submission triggered");

        const formData = new FormData(this);

        // ✅ CSRF check
        if (typeof csrftoken === "undefined") {
            const csrfEl = document.querySelector('[name=csrfmiddlewaretoken]');
            if (csrfEl) formData.append("csrfmiddlewaretoken", csrfEl.value);
        } else {
            formData.append("csrfmiddlewaretoken", csrftoken);
        }

        // ✅ User type check
        if (!formData.get("user_registration_type")) {
            const savedType = localStorage.getItem("user_registration_type");
            if (savedType) {
                formData.set("user_registration_type", savedType);
                console.log("Added saved user_registration_type:", savedType);
            } else {
                console.warn("No user_registration_type found.");
                toastr.error("Registration type missing — please restart registration.");
                return;
            }
        }

        console.log("Submitting Arbitrator form with data:", Object.fromEntries(formData.entries()));

        $.ajax({
            type: "POST",
            url: "/user_registration",
            data: formData,
            cache: false,
            contentType: false,
            processData: false,
            success: function (response) {
                toastr.success(response.message || "Form submitted successfully!");
                console.log("Arbitrator Registration Success:", response);
            },
            error: function (xhr) {
                console.error("Arbitrator Registration Error:", xhr.status, xhr.responseText);
                let errMsg = xhr.responseJSON?.error || xhr.statusText || "Submission failed";
                toastr.error(errMsg);
            },
        });
    });
});
