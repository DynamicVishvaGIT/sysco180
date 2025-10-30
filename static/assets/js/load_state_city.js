let state_data = [`<option value="" disabled selected>Select State</option>`];
let city_data = [`<option value="" disabled selected>Select City</option>`];

$(document).ready(function () {
    load_state();
    // Only init select2 after loading options
    // $(".state_data").select2({
    //     placeholder: "Select State",
    //     allowClear: true,
    //     width: '100%'
    // });

    // $(".city_data").select2({
    //     placeholder: "Select City",
    //     allowClear: true,
    //     width: '100%'
    // });
});

function load_state() {
    $.ajax({
        url: "/load_state",
        success: function (response) {
            state_data = [`<option value="" disabled selected>Select State</option>`];
            $.each(response.data, function (i, v) {
                state_data.push(`<option value="${v.id}">${v.NAME}</option>`);
            });
            $(".state_data").html(state_data).trigger('change');
        }
    });
}

$(".state_data").on("change", function () {
    const state_id = $(this).val();
    // $(".city_info").hide();

    if (!state_id || state_id === "null") {
        $(".city_data").html(`<option value="" disabled selected>Select City</option>`).trigger('change');
        return;
    }

    $.ajax({
        url: `/dropdown_city?state_id=${state_id}`,
        success: function (response) {
            city_data = [`<option value="" disabled selected>Select City</option>`];
            $.each(response, function (i, v) {
                city_data.push(`<option value="${v.id}">${v.NAME}</option>`);
            });
            $(".city_data").html(city_data).trigger('change');
            $(".city_info").hide();

        }
    });
});



