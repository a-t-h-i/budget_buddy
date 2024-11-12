<script lang="ts">
	import Highcharts from 'highcharts';
	import Chart from '@highcharts/svelte';

	let series: Highcharts.SeriesLineOptions = {
		type: 'line',
		name: 'Jane',
		data: [1, 0, 4]
	};

	function addRandomPointToSeries() {
		series.data?.push(Math.random());
		series.data = series.data;
	}

	let options: Highcharts.Options;

	$: options = {
		title: {
			text: 'Numbers',
			floating: true,
		},
		xAxis: {
			categories: ['Apples', 'Bananas', 'Oranges']
		},
		yAxis: {
			title: {
				text: 'Fruit eaten'
			}
		},
		series: [series],
		chart: {
			style: {
				borderRadius: 10,
				
			}
		}
        

	};
</script>


<div class="grid lg:grid-cols-4 items-center sm:grid-cols-2">
	<div class="p-2">
		<Chart {options}/>
	</div>

    <div class="p-2">
		<Chart {options}/>
	</div>

    <div class="p-2">
		<Chart {options}/>
	</div>

    <div class="p-2">
		<Chart {options}/>
	</div>

    <button on:click={addRandomPointToSeries} class="btn shadow-md w-[60px]">Add</button>
</div>
