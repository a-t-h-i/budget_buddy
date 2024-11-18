<script lang="ts">
	import Highcharts from 'highcharts';
	import Chart from '@highcharts/svelte';

	let expenseTrends: Highcharts.SeriesLineOptions = {
		type: 'line',
		name: 'R',
		data: [54.31, 900.12, 344.1, 120.45, 76.89, 45.67, 980.22, 23.89, 450.34, 198.76]
	};

	let expenseDates = [
				'28-01-2034', 
				'29-01-2034', 
				'30-01-2034', 
				'31-01-2034', 
				'01-02-2034', 
				'02-02-2034', 
				'03-02-2034', 
				'04-02-2034', 
				'05-02-2034', 
				'06-02-2034'
			];


	let options: Highcharts.Options;

	$: options = {
		title: {
			text: "Daily Spending Trends",
		},
		xAxis: {
			categories: expenseDates,
		},
		yAxis: {
			title: {
				text: 'Total Spent'
			}
		},
		series: [expenseTrends],
		chart: {
			style: {
				borderRadius: 10,
			}
		}
	};


</script>


<div class="grid lg:grid-cols-2 items-center sm:grid-cols-2">
	<div class="p-2 sm:w-fit">
		<Chart {options}/>
	</div>

    <div class="p-2 sm:w-fit">
		<Chart {options}/>
	</div>
</div>
