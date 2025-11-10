// Role selection handling
//     document.querySelectorAll('.role-item').forEach(item=>{
//       item.addEventListener('click', () => {
//         document.querySelectorAll('.role-item').forEach(i=>i.classList.remove('active'));
//         item.classList.add('active');
//         const title = item.querySelector('div > div').innerText || item.dataset.role;
//         document.getElementById('selectedRole').innerText = title;
//       });
//     });

//     // OTP / SSO toggle
//     const tOtp = document.getElementById('toggle-otp');
//     const tSso = document.getElementById('toggle-sso');
//     const emailSection = document.getElementById('emailSection');

//     function setToggle(which){
//       if(which === 'otp'){
//         tOtp.classList.add('active');
//         tSso.classList.remove('active');
//         emailSection.style.display = 'block';
//       } else {
//         tOtp.classList.remove('active');
//         tSso.classList.add('active');
//         emailSection.style.display = 'none';
//       }
//     }
//     tOtp.addEventListener('click', ()=>setToggle('otp'));
//     tSso.addEventListener('click', ()=>setToggle('sso'));
//     setToggle('otp');

//     // Send OTP simulation
//     document.getElementById('sendOtpBtn').addEventListener('click', ()=>{
//       const email = document.getElementById('emailInput').value.trim();
//       if(!email){
//         alert('Please enter your email address.');
//         return;
//       }
//       // Simple simulated action
//       const role = document.getElementById('selectedRole').innerText;
//       document.getElementById('sendOtpBtn').disabled = true;
//       document.getElementById('sendOtpBtn').innerHTML = 'Sending...';
//       setTimeout(()=>{
//         document.getElementById('sendOtpBtn').innerHTML = 'OTP Sent ✓';
//         // revert back after short time
//         setTimeout(()=>{
//           document.getElementById('sendOtpBtn').innerHTML = 'Send OTP <i class="bi bi-arrow-right ms-2"></i>';
//           document.getElementById('sendOtpBtn').disabled = false;
//         }, 1800);
//       }, 900);
//     });

//     // Register arbitrator click
//     document.getElementById('registerArb').addEventListener('click', (e)=>{
//       e.preventDefault();
//       alert('Register flow placeholder — open registration form/modal here.');
//     });

//     // Accessibility: allow role-item activation with keyboard
//     document.querySelectorAll('.role-item').forEach(item=>{
//       item.tabIndex = 0;
//       item.addEventListener('keydown', (ev)=>{
//         if(ev.key === 'Enter' || ev.key === ' '){
//           ev.preventDefault();
//           item.click();
//         }
//       });
//     });

// document.addEventListener("DOMContentLoaded", () => {

//     console.log("✅ script.js loaded");
//     const sendOtpBtn = document.getElementById("sendOtpBtn");
//     const backBtn = document.getElementById("backBtn");
//     const emailSection = document.getElementById("emailSection");
//     const sendOtpSection = document.getElementById("sendOtpSection");
//     const otpSection = document.getElementById("otpSection");
//     const otpInput = document.getElementById("otpInput");
//     const verifyBtn = document.getElementById("verifyBtn");
//     const emailInput = document.getElementById("emailInput");

//     // On "Send OTP" click → Hide Email, Show OTP
//     sendOtpBtn.addEventListener("click", () => {
//         if (emailInput.value.trim() === "") {
//             alert("Please enter your email first!");
//             return;
//         }
//         emailSection.style.display = "none";
//         sendOtpSection.style.display = "none";
//         otpSection.style.display = "";
//         otpInput.focus();
//     });

//     // On "Back" click → Show Email, Hide OTP
//     backBtn.addEventListener("click", () => {
//         emailSection.style.display = "block";
//         sendOtpSection.style.display = "block";
//         otpSection.style.display = "";
//         otpInput.value = "";
//         verifyBtn.disabled = true;
//     });

//     // Enable Verify button only when 6 digits entered
//     otpInput.addEventListener("input", () => {
//         if (otpInput.value.length === 6 && /^\d+$/.test(otpInput.value)) {
//             verifyBtn.disabled = false;
//         } else {
//             verifyBtn.disabled = true;
//         }
//     });

//     // Example Verify button action
//     verifyBtn.addEventListener("click", () => {
//         alert("OTP Verified Successfully!");
//     });
// });

// document.addEventListener("DOMContentLoaded", () => {
//   const registerBtn = document.getElementById("registerArb"); // Sign Up btn
//   const formBox = document.getElementById("formBox"); // Registration card
//   const registerBox = document.getElementById("registerBox"); // "New User?" box
//   const regBackBtn = document.getElementById("regBackBtn"); // Back btn in form

//   if (registerBtn && formBox && registerBox && regBackBtn) {
//     // Show form when Sign Up clicked
//     registerBtn.addEventListener("click", () => {
//       registerBox.style.display = "none";
//       formBox.style.display = "block";
//     });

//     // Go back when Back clicked
//     regBackBtn.addEventListener("click", () => {
//       formBox.style.display = "none";
//       registerBox.style.display = "block";
//     });
//   }
// });


// document.addEventListener("DOMContentLoaded", function () {
//   // Personal form submit
//   const form = document.getElementById("personalForm");
//   if (form) {
//     form.addEventListener("submit", function (e) {
//       e.preventDefault();

//       const data = {
//         firstName: document.getElementById("firstName").value,
//         lastName: document.getElementById("lastName").value,
//         email: document.getElementById("email").value,
//         phone: document.getElementById("phone").value,
//         organization: document.getElementById("organization").value
//       };

//       localStorage.setItem("userData", JSON.stringify(data));
//       window.location.href = "review_submit.html";
//     });
//   }

//   // Review page load
//   if (window.location.pathname.includes("review_submit.html")) {
//     const saved = JSON.parse(localStorage.getItem("userData")) || {};

//     document.getElementById("reviewName").textContent = (saved.firstName || "") + " " + (saved.lastName || "");
//     document.getElementById("reviewEmail").textContent = saved.email || "";
//     document.getElementById("reviewPhone").textContent = saved.phone || "";
//     document.getElementById("reviewOrg").textContent = saved.organization || "";

//     // Submit → redirect login
//     const submitBtn = document.getElementById("submitBtn");
//     if (submitBtn) {
//       submitBtn.addEventListener("click", function () {
//         localStorage.removeItem("userData"); // clear
//         window.location.href = "login.html";
//       });
//     }
//   }
// });


// document.addEventListener('DOMContentLoaded', () => {
//     const sendOtpBtn = document.getElementById('sendOtpBtn');
//     const otpSection = document.getElementById('otpSection');
//     const otpInput = document.getElementById('otpInput');
//     const verifyBtn = document.getElementById('verifyBtn');
//     const backBtn = document.getElementById('backBtn');
//     const emailInput = document.getElementById('emailInput');

//     // Send OTP click
//     sendOtpBtn.addEventListener('click', () => {
//         if(emailInput.value.trim() === "") {
//             alert("Please enter your email first!");
//             emailInput.focus();
//             return;
//         }

//         // Show OTP section
//         otpSection.classList.remove('d-none');
//         otpInput.focus();

//         // Optional: disable email input
//         emailInput.disabled = true;
//     });

//     // Enable Verify button when OTP length is 6
//     otpInput.addEventListener('input', () => {
//         verifyBtn.disabled = otpInput.value.length !== 6;
//     });

//     // Back button hides OTP section
//     backBtn.addEventListener('click', () => {
//         otpSection.classList.add('d-none'); // hide OTP
//         otpInput.value = '';
//         verifyBtn.disabled = true;
//         emailInput.disabled = false;
//         emailInput.focus();
//     });
// });


$("#sendOtpBtn").click(function () { 
    $("#emailSection_1").css("display","none");
    $("#otpSection").css("display","block");

});

$("#backBtn").click(function () {
    $("#emailSection_1").css("display","flex");
    $("#otpSection").css("display","none");
});

$(document).ready(function() {
  // get current page filename (like sessions.php)
  var currentPage = window.location.pathname.split("/").pop();
  $(".nav-link.btn-upload").each(function() {
    var linkPage = $(this).attr("href");

    if (linkPage === `/${currentPage}`) {
      $(this).addClass("active");
    }
  });
});