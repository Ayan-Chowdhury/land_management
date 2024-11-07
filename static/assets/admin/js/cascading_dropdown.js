// static/admin/js/cascading_dropdown.js
(function($) {
    $(document).ready(function() {
        $('#id_Division').change(function() {
            var divisionCode = $(this).val();
            $.ajax({
                url: '/filter_districts/',
                data: {
                    'division': divisionCode
                },
                success: function(data) {
                    var districtSelect = $('#id_District');
                    districtSelect.empty();
                    districtSelect.append('<option value="">---------</option>');
                    $.each(data, function(index, item) {
                        districtSelect.append('<option value="' + item.DistrictCode + '">' + item.DistrictName + '</option>');
                    });
                    $('#id_Upazilla').html('<option value="">---------</option>');  // Clear Upazilla options
                }
            });
        });

        $('#id_District').change(function() {
            var districtCode = $(this).val();
            $.ajax({
                url: '/filter_upazillas/',
                data: {
                    'district': districtCode
                },
                success: function(data) {
                    var upazillaSelect = $('#id_Upazilla');
                    upazillaSelect.empty();
                    upazillaSelect.append('<option value="">---------</option>');
                    $.each(data, function(index, item) {
                        upazillaSelect.append('<option value="' + item.UpazillaCode + '">' + item.UpazillaName + '</option>');
                    });
                }
            });
        });
    });
})(django.jQuery);
