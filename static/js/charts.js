// PIE GRAPH - PALETTE GENERATOR
// https://learnui.design/tools/data-color-picker.html#palette

function hardwareStatusPieChart(input_data) {
	const labels = ["Unassigned", "To be delivered", "Delivered", "Returning", "Returned", "Kept"];
	const data = {
		labels: labels,
		datasets: [
			{
				label: "My First Dataset",
				data: input_data,
				backgroundColor: ["#003f5c", "#494d87", "#994f94", "#df5080", "#ff6e52", "#ffa600"],
				hoverOffset: 4,
			},
		],
	};
	const config = {
		type: "doughnut",
		data: data,
		options: {
			plugins: {
				title: {
					display: true,
					text: "Hardware Status Pie Chart",
				},
			},
		},
	};
	const myChart = new Chart(document.getElementById("hardware_Status_pie_chart"), config);
}

function hardwareStatusPolarAreaChart(input_data) {
	const labels = ["Unassigned", "To be delivered", "Delivered", "Returning", "Returned", "Kept"];
	const data = {
		labels: labels,
		datasets: [
			{
				label: "My First Dataset",
				data: input_data,
				backgroundColor: ["#003f5c", "#494d87", "#994f94", "#df5080", "#ff6e52", "#ffa600"],
				hoverOffset: 4,
			},
		],
	};
	const config = {
		type: "polarArea",
		data: data,
		options: {
			plugins: {
				title: {
					display: true,
					text: "Hardware Status Polar Area Chart",
				},
			},
		},
	};
	const myChart = new Chart(document.getElementById("hardware_Status_polar_area_chart"), config);
}

function hardwareStatusBarChart(input_data) {
	const labels = ["Unassigned", "To be delivered", "Delivered", "Returning", "Returned", "Kept"];
	const data = {
		labels: labels,
		datasets: [
			{
				label: "My First Dataset",
				data: input_data,
				backgroundColor: ["#003f5c", "#494d87", "#994f94", "#df5080", "#ff6e52", "#ffa600"],
				hoverOffset: 4,
			},
		],
	};
	const config = {
		type: "bar",
		data: data,
		options: {
			plugins: {
				title: {
					display: true,
					text: "Hardware Status Bar Chart",
				},
			},
		},
	};
	const myChart = new Chart(document.getElementById("hardware_Status_bar_chart"), config);
}
