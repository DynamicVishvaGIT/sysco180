console.log("Bank User Upload Cases");


$("body").on("click", ".add_btn", function () {
    let form = $(this).closest("form");
    let form_id = form.attr("id");
    clone_party(form_id);
});

function clone_party(form_id) {
    let total_party = $(`#${form_id} .clone_doc_form`).length + 1;

    if (total_party > 10) {
        toastr.info("You cannot add more than 10 party details.");
        return;
    }

    let html = `
     <div class="row g-3 mb-2 party-group align-items-end clone_doc_form">

        <!-- Party Name -->
        <div class="col-lg-5 col-md-6">
            <label class="form-label">Party Name</label>
            <input type="text" class="form-control form_control" name="party_name" placeholder="Enter party name">
        </div>

        <!-- Party Address -->
        <div class="col-lg-5 col-md-6">
            <label class="form-label">Party Address</label>
            <textarea class="form-control form_control" name="party_address" rows="2" placeholder="Enter address with pincode"></textarea>
        </div>

        <!-- Plus / Minus Buttons -->
        <div class="col-lg-1 col-md-12 d-flex align-items-end gap-2 mb-4">
            <button type="button" class="btn btn-success w-100 add_btn">+</button>
            <button type="button" class="btn btn-danger w-100 remove_btn">-</button>
        </div>

    </div>`;

    $(`#${form_id} #emp_doc`).append(html);
}

$("body").on("click", ".remove_btn", function () {
    let form = $(this).closest("form");
    let form_id = form.attr("id");
    let total_party = $(`#${form_id} .party-group`).length;

    if (total_party === 1) {
        toastr.info("At least one party detail is required.");
        return;
    }

    $(this).closest(".party-group").remove();
});


$("#create_single_case_form").on('submit', function (e) {
    e.preventDefault();

    let submitBtn = $("#create_single_case_form button[type=submit]");
    submitBtn.prop("disabled", true).text("Creating...");

    var formData = new FormData(this);

    $.ajax({
        type: "POST",
        url: "/create_single_case",
        data: formData,
        cache: false,
        contentType: false,
        processData: false,
        success: function (response) {

            toastr.success(response.message);

            $('#create_single_case_form')[0].reset();
            submitBtn.prop("disabled", false).text("Submit");

        },
        error: function (response) {
            toastr.error(response.responseJSON?.message);
            submitBtn.prop("disabled", false).text("Submit");
        }
    });
});


if ($.fn.DataTable.isDataTable('#my_cases_table_id')) {
    $('#my_cases_table_id').DataTable().clear().destroy();
}

var t = $('#my_cases_table_id').DataTable({
    ajax: 'load_cases',
    processing: true,
    responsive: true,
    columns: [
        {
            data: null,
            render: function (data, type, row, meta) {
                return meta.row + 1;
            }
        },
        { data: 'CUSTOMER_NAME' },
        { data: 'EMAIL_ID' },
        {
            data: 'PARTY_NAMES',
            render: function(data){
                return data.length ? data.join(' vs ') : '-';
            }
        },
        { data: 'UPLOAD_DATE' },
        { data: 'ADVOCATE_NAME' },
        { data: 'ARBITRATOR_NAME' },
        {
            data: null,
            render: function (data) {
                return `
                <div class="dropdown">
                    <button class="btn btn-primary dropdown-toggle" data-bs-toggle="dropdown">Action</button>
                    <div class="dropdown-menu">
                        <a href="/my_cases_view/${data.id}" class="dropdown-item view_case_details" data-id="${data.id}"><i class="fa fa-eye"></i> View Details</a>
                        <a href="javascript:void(0)" class="dropdown-item edit_case" data-id="${data.id}"><i class="fa fa-pencil"> </i> Edit</a>
                        <a href="javascript:void(0)" class="dropdown-item delete_case" data-id="${data.id}"><i class="fa fa-trash"> </i> Delete</a>

                    </div>
                </div>`;
            }
        }
    ]
});



$("#bulk_upload_form").on("submit", function (e) {
    e.preventDefault();

    let file = $("#bulk_cases_excel_sheet").val();

    if (!file) {
        toastr.error("Please select your excel sheet to upload");
        return;
    }

    let formData = new FormData(this);

    $.ajax({
        url: "/upload_bulk_cases",
        type: "POST",
        data: formData,
        processData: false,
        contentType: false,
        beforeSend: function () {
            $(".submit_btn").prop("disabled", true).text("Uploading...");
        },
        success: function (response) {
            toastr.success(response.message);
            $("#bulk_upload_form")[0].reset();
        },
        error: function (xhr) {
            toastr.error(xhr.responseJSON.message);
        },
        complete: function () {
            $(".submit_btn").prop("disabled", false).text("Upload Now");
        }
    });
});

