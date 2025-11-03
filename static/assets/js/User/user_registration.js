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


// User Login & OTP Verification -------------------------------------------->


$(document).ready(function () {

    let selectedRole = null;

    // --------------------------
    // ROLE SELECTION HANDLER
    // --------------------------
    $(".role-item").on("click", function () {
        $(".role-item").removeClass("active-role");
        $(this).addClass("active-role");
        selectedRole = $(this).data("role");

        console.log("Selected Role:", selectedRole);

        // Show email/phone section after role is selected
        $("#emailSection_1").slideDown();

        // Reset OTP section
        $("#otpSection").hide();
    });

    // --------------------------
    // SEND OTP BUTTON
    // --------------------------
    $("#sendOtpBtn").on("click", function (e) {
        e.preventDefault();

        let mobile_no_email = $("#mobile_no_email").val()?.trim();

        if (!selectedRole) {
            toastr.warning("Please select your role first.");
            return;
        }

        if (!mobile_no_email) {
            toastr.warning("Please enter your Email / Mobile number.");
            return;
        }

        // Disable button while sending
        $("#sendOtpBtn").prop("disabled", true).text("Sending...");

        $.ajax({
            url: "/send_otp",
            type: "POST",
            data: {
                mobile_no_email: mobile_no_email,
                user_type: selectedRole,
                otp_for: "login"
            },
            success: function (response) {
                toastr.success(response.message );

                // Show OTP section
                $("#emailSection_1").hide();
                $("#otpSection").slideDown();

                // Save for later use
                localStorage.setItem("user_type", selectedRole);
                localStorage.setItem("mobile_no_email", mobile_no_email);
            },
            error: function (xhr) {
                let msg = "Something went wrong!";
                if (xhr.responseJSON && xhr.responseJSON.message) {
                    msg = xhr.responseJSON.message;
                }
                toastr.error(msg);
            },
            complete: function () {
                $("#sendOtpBtn").prop("disabled", false).html('Send OTP <i class="bi bi-arrow-right ms-2"></i>');
            }
        });
    });

    // --------------------------
    // VERIFY OTP BUTTON
    // --------------------------
   // --------------------------
// VERIFY OTP BUTTON
// --------------------------
$("#verifyBtn").on("click", function (e) {
    e.preventDefault();

    let otp = $("#otpInput").val()?.trim();
    let mobile_no_email = localStorage.getItem("mobile_no_email");
    let user_type = localStorage.getItem("user_type");

    // Strict validation for 6 digits
    if (!/^\d{4}$/.test(otp)) {
        toastr.error("Please enter a valid 4-digit OTP.");
        return;
    }

    $("#verifyBtn").prop("disabled", true).text("Verifying...");

    $.ajax({
        url: "/verify_otp",
        type: "POST",
        data: {
            mobile_no_email: mobile_no_email,
            user_type: user_type,
            otp: otp
        },
        success: function (response) {
            // show server message or otp for testing
            toastr.success(response.message || "OTP verified successfully!");

            // Redirect after verification based on role (only on success)
            if (user_type === "bank_individual") {
                window.location.href = "/bank_user_dashboard";
            } else if (user_type === "admin") {
                window.location.href = "/admin_dashboard";
            } else if (user_type === "arbitrator") {
                window.location.href = "/arbitrator_dashboard";
            } else if (user_type === "mediator") {
                window.location.href = "/mediator_dashboard";
            } else {
                window.location.href = "/";
            }
        },
        error: function (xhr) {
            let msg = "Invalid OTP or Server Error.";
            if (xhr.responseJSON && xhr.responseJSON.message) {
                msg = xhr.responseJSON.message;
            }
            toastr.error(msg);
        },
        complete: function () {
            $("#verifyBtn").prop("disabled", false).text("Verify & Sign In");
        }
    });
});

    // --------------------------
    // BACK BUTTON
    // --------------------------
    $("#backBtn").on("click", function () {
        $("#otpSection").hide();
        $("#emailSection_1").slideDown();
    });

});


