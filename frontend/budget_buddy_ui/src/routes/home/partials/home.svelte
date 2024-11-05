<script lang="ts">
	import * as echarts from 'echarts';
	import { onMount } from 'svelte';
	import * as Table from "$lib/components/ui/table/index.js";
	onMount(() => {
		let myChart = echarts.init(document.getElementById('pieChart'));
		// Draw the chart
		
		myChart.setOption({
			title: {
				text: 'Income Distribution',
			},
			tooltip: {},
			xAxis: {
				data: ['Expenses', 'Savings', 'Investment']
			},
			yAxis: {},
			series: [
				{
					name: 'sales',
					type: 'pie',
					data: [50,20,30]
				},
			]
		});

        let barChart = echarts.init(document.getElementById('barChart'));
        barChart.setOption({
			title: {
				text: 'Expenses'
			},
			tooltip: {},
			xAxis: {
				data: ['shirt', 'cardigan', 'chiffon', 'pants', 'heels', 'socks']
			},
			yAxis: {},
			series: [
				{
					name: 'sales',
					type: 'bar',
					data: [5, 20, 36, 10, 10, 20]
				}
			]
		});

        let lineChart = echarts.init(document.getElementById('lineChart'));
        lineChart.setOption({
			title: {
				text: 'Closing Balance'
			},
			tooltip: {},
			xAxis: {
				data: ['January', 'February', 'March', 'April', 'May', 'June']
			},
			yAxis: {},
			series: [
				{
					name: 'Closing Balance',
					type: 'line',
					data: [233.0, 11.41, 336, 140, 610, 120]
				}
			]
		});

	});

	let expenseItems = $state([
    {
        name: 'Groceries',
        price: 49.99,
        date: '01 September 2024',
        category: 'Food',
        budget: 'December Budget',
        type: 'recurring'
    },
    {
        name: 'Electricity',
        price: 49.02,
        date: '03 September 2024',
        category: 'Utilities',
        budget: 'October Budget',
        type: 'recurring'
    },
    {
        name: 'Internet',
        price: 400.29,
        date: '05 September 2024',
        category: 'Utilities',
        budget: 'November Budget',
        type: 'recurring'
    },
    {
        name: 'Water',
        price: 75.50,
        date: '10 September 2024',
        category: 'Utilities',
        budget: 'September Budget',
        type: 'recurring'
    },
    {
        name: 'Rent',
        price: 4000.00,
        date: '01 October 2024',
        category: 'Housing',
        budget: 'October Budget',
        type: 'recurring'
    },
    {
        name: 'Dining Out',
        price: 120.75,
        date: '15 September 2024',
        category: 'Entertainment',
        budget: 'September Budget',
        type: 'once-off'
    },
    {
        name: 'Gym Membership',
        price: 150.00,
        date: '20 September 2024',
        category: 'Health',
        budget: 'September Budget',
        type: 'recurring'
    },
    {
        name: 'Transportation',
        price: 60.00,
        date: '25 September 2024',
        category: 'Travel',
        budget: 'September Budget',
        type: 'once-off'
    }
]);

</script>

<div>
	<!-- Graphs -->
	<div class="grid lg:grid-cols-4 sm:grid-cols-2">
		<div class="border rounded-xl lg:h-[20vw] m-1 p-2 hover:shadow-md transition duration-500 ease-in-out" id="pieChart"></div>
		<div class="border rounded-xl lg:h-[20vw] m-1 p-2 hover:shadow-md transition duration-500 ease-in-out" id="barChart"></div>
		<div class="border rounded-xl lg:h-[20vw] m-1 col-span-2 p-2  hover:shadow-md transition duration-500 ease-in-out" id="lineChart"></div>
	</div>

	<!-- Table -->
	<div>
		<div class="lg:h-[100%] m-1 col-span-2">
			

			<Table.Root class="p-2">
			
				<Table.Header>
				  <Table.Row>
					<Table.Head class="text-black">Date</Table.Head>
					<Table.Head class="text-black">Name</Table.Head>
					<Table.Head class="text-black">Category</Table.Head>
					<Table.Head class="text-black">Budget</Table.Head>
					<Table.Head class="text-black text-center">Amount</Table.Head>
				  </Table.Row>
				</Table.Header>

				<Table.Body>
				  {#each expenseItems as expense}
					<Table.Row class="hover:bg-gray-200transition duration-500 ease-in-out">
					  <Table.Cell class="">{expense.date}</Table.Cell>
					  <Table.Cell class="">{expense.name}</Table.Cell>
					  <Table.Cell class=""><span class="badge">{expense.category}</span></Table.Cell>
					  <Table.Cell class="">{expense.budget}</Table.Cell>
					  <Table.Cell class="text-center">R {expense.price}</Table.Cell>
					</Table.Row>
				  {/each}
				</Table.Body>
			</Table.Root>
		</div>
	</div>
</div>
