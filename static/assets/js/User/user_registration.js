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

    const selectedType = $("#user_registration_type").val();
    const termsAccepted = $("#termsCheck").is(":checked");

    if (!selectedType) {
        toastr.error("Please select a registration type before continuing.");
        return;
    }
    if (!termsAccepted) {
        toastr.error("Please accept the Terms and Conditions.");
        return;
    }

    $.ajax({
        type: "POST",
        url: "/user_type",
        headers: {
            "X-CSRFToken": csrftoken,
        },
        data: {
            user_registration_type: selectedType.toLowerCase(),
            terms_and_conditions: termsAccepted ? "true" : "false",
        },
        success: function (response) {

            const userType = (response.user_type || "").toLowerCase();
            const terms = response.terms_and_conditions || "false";

            if (!userType) {
                toastr.error("User type missing in response.");
                return;
            }

            localStorage.setItem("user_registration_type", userType);
            localStorage.setItem("terms_and_conditions", terms);

            toastr.success("User type saved: " + userType);

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
            toastr.error(xhr.responseJSON?.error || "Something went wrong while contacting the server.");
        },
    });
});

$(document).ready(function() {
    const userType = localStorage.getItem("user_registration_type");
    const terms = localStorage.getItem("terms_and_conditions");

    if (userType) {
        $("#user_type_display").text(userType.toUpperCase());
    } else {
        console.warn(" No user_registration_type found in localStorage.");
        toastr.warning("Registration type not found — please restart registration.");
    }

});

// Arbitrator Registration Form--------->

$(document).ready(function () {
    $("#arbitrator_registration_form").on("submit", function (e) {
        e.preventDefault();

        const formData = new FormData(this);
        const userType = localStorage.getItem("user_registration_type") || "";
        const terms = localStorage.getItem("terms_and_conditions") || "false";

        formData.append("user_registration_type", userType);
        formData.append("terms_and_conditions", terms);

        $.ajax({
            type: "POST",
            url: "/user_registration",
            data: formData,
            cache: false,
            contentType: false,
            processData: false,
            success: function (response) {
                    toastr.success(response.message);
                    const id      = response.id;
                    const user_type = response.type
                   setTimeout(function () {
                    window.location.href = `/view_registration_details/${id}?type=${user_type}`;
                    }, 1000);
            },
            error: function (xhr) {
                console.error("Registration Error:", xhr.status, xhr.responseText);
                toastr.error("Error submitting form");
            },
        });
    });
});

// Mediator Registration Form  --------->

$(document).ready(function () {
    $("#mediator_registration_Form").on("submit", function (e) {
        e.preventDefault();

        const formData = new FormData(this);   
         const userType = localStorage.getItem("user_registration_type") || "";
        const terms = localStorage.getItem("terms_and_conditions") || "false";

        formData.append("user_registration_type", userType);
        formData.append("terms_and_conditions", terms);  

        $.ajax({
            type: "POST",
            url: "/user_registration",
            data: formData,
            cache: false,
            contentType: false,
            processData: false,
            success: function (response) {
                    toastr.success(response.message);
                    const id      = response.id;
                    const user_type = response.type
                   setTimeout(function () {
                    window.location.href = `/view_registration_details/${id}?type=${user_type}`;
                    }, 1000);

            },
            error: function (xhr) {
                console.error("Mediator Registration Error:", xhr.status, xhr.responseText);

                toastr.error(errMsg);
            },
        });
    });
});


// Bank / Individual / Personal information Form  --------->

$(document).ready(function () {
    $("#personal_information_form").on("submit", function (e) {
        e.preventDefault();

        const formData = new FormData(this);

        const userType = localStorage.getItem("user_registration_type") || "";
        const terms = localStorage.getItem("terms_and_conditions") || "false";

        formData.append("user_registration_type", userType);
        formData.append("terms_and_conditions", terms);

        $.ajax({
            type: "POST",
            url: "/user_registration",
            data: formData,
            cache: false,
            contentType: false,
            processData: false,
            success: function (response) {
               toastr.success(response.message);
                    const id        = response.id;
                    const user_type = response.type
                   setTimeout(function () {
                    window.location.href = `/view_registration_details/${id}?type=${user_type}`;
                    }, 1000);
            },
            error: function (xhr) {
                console.error("Bank Individual Registration Error:", xhr.status, xhr.responseText);
                toastr.error(xhr.responseJSON?.error);
            },
        });
    });
});
