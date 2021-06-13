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

$("#id_save_object").click(function () {
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

function deleteObject(api, id) {
	var message = "Are you sure?";
	confirmDialog(message, function () {
		$.ajax({
			url: "/api/" + api.toLowerCase() + "/" + id + "/",
			method: "DELETE",
			headers: { "X-CSRFToken": $("input[name=csrfmiddlewaretoken]").val() },
			contentType: "application/json; charset=UTF-8",
			dataType: "json",
			success: function (data) {
				location.href = "/" + api.toLowerCase() + "/";
			},
			error: function () {
				alert("ajax delete error");
			},
		});
	});
}

function confirmDialog(message, onConfirm) {
	var fClose = function () {
		modal.modal("hide");
	};
	var modal = $("#confirmModal");
	modal.modal("show");
	$("#confirmMessage").empty().append(message);
	$("#confirmOk").unbind().one("click", onConfirm).one("click", fClose);
	$("#confirmCancel").unbind().one("click", fClose);
}
