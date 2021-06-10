$("#id_create_modal").click(function () {
	var endpoint = this.value;
	var new_data = {};
	$("#modalBody")
		.children()
		.each(function () {
			key = this.id.replace("id_", "");
			value = this.value;
			if (value == "") {
				value = null;
			}
			new_data[key] = value;
		});
	$.ajax({
		url: "/api/" + endpoint.toLowerCase() + "/",
		method: "POST",
		headers: { "X-CSRFToken": $("input[name=csrfmiddlewaretoken]").val() },
		data: JSON.stringify(new_data),
		contentType: "application/json; charset=UTF-8",
		dataType: "json",
		success: function (data) {
			location.href = "/" + endpoint.toLowerCase();
		},
		error: function () {
			alert("ajax post error");
		},
	});
});

$("#save_object").click(function () {
	var endpoint = this.value;
	var new_data = {};
	$("#form_edit")
		.children()
		.each(function () {
			key = this.id.replace("id_", "");
			value = this.value;
			if (value == "") {
				value = null;
			}
			new_data[key] = value;
		});
	$.ajax({
		url: "/api/" + endpoint.toLowerCase() + "/",
		method: "PATCH",
		headers: { "X-CSRFToken": $("input[name=csrfmiddlewaretoken]").val() },
		data: JSON.stringify(new_data),
		contentType: "application/json; charset=UTF-8",
		dataType: "json",
		success: function (data) {
			location.href = "/" + endpoint.split("/")[0].toLowerCase();
		},
		error: function () {
			alert("ajax post error");
		},
	});
});
