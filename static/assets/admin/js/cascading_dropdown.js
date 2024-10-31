// static/admin/js/cascading_dropdown.js
(function($) {
    $(document).ready(function() {
        // Fetch Districts based on Division
        $('#id_Division').change(function() {
            var divisionId = $(this).val();
            if (divisionId) {
                $.ajax({
                    url: '/filter_districts/?division=' + divisionId,
                    method: 'GET',
                    success: function(data) {
                        var districtSelect = $('#id_District');
                        districtSelect.empty();
                        districtSelect.append('<option value="">---------</option>');
                        $.each(data, function(index, district) {
                            districtSelect.append('<option value="' + district.DistrictCode + '">' + district.DistrictName + '</option>');
                        });
                        // Reset Upazilla selection
                        $('#id_Upazilla').empty().append('<option value="">---------</option>');
                    }
                });
            } else {
                $('#id_District').empty().append('<option value="">---------</option>');
                $('#id_Upazilla').empty().append('<option value="">---------</option>');
            }
        });

        // Fetch Upazillas based on District
        $('#id_District').change(function() {
            var districtId = $(this).val();
            if (districtId) {
                $.ajax({
                    url: '/filter_upazillas/?district=' + districtId,
                    method: 'GET',
                    success: function(data) {
                        var upazillaSelect = $('#id_Upazilla');
                        upazillaSelect.empty();
                        upazillaSelect.append('<option value="">---------</option>');
                        $.each(data, function(index, upazilla) {
                            upazillaSelect.append('<option value="' + upazilla.UpazillaCode + '">' + upazilla.UpazillaName + '</option>');
                        });
                    }
                });
            } else {
                $('#id_Upazilla').empty().append('<option value="">---------</option>');
            }
        });
    });
})(django.jQuery);
