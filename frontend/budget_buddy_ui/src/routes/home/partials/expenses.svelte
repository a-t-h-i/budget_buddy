<script lang="ts">
	import { Button } from '$lib/components/ui/button/index.js';
	import * as Card from '$lib/components/ui/card/index.js';
	import { Badge } from '$lib/components/ui/badge/index.js';
	import { buttonVariants } from '$lib/components/ui/button/index.js';
	import * as Dialog from '$lib/components/ui/dialog/index.js';
	import { Input } from '$lib/components/ui/input/index.js';
	import { Label } from '$lib/components/ui/label/index.js';
	import * as Select from '$lib/components/ui/select/index.js';
	import DatePicker from './date_picker.svelte';
	
	let expenseItems = $state([
		
		{
			name: 'Rent',
			price: 4000.0,
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
			price: 150.0,
			date: '20 September 2024',
			category: 'Health',
			budget: 'September Budget',
			type: 'recurring'
		},
		{
			name: 'Transportation',
			price: 60.0,
			date: '25 September 2024',
			category: 'Travel',
			budget: 'September Budget',
			type: 'once-off'
		},
		{
			name: 'Transportation',
			price: 60.0,
			date: '25 September 2024',
			category: 'Travel',
			budget: 'September Budget',
			type: 'once-off'
		},
		{
			name: 'Transportation',
			price: 60.0,
			date: '25 September 2024',
			category: 'Travel',
			budget: 'September Budget',
			type: 'once-off'
		},
		{
			name: 'Transportation',
			price: 60.0,
			date: '25 September 2024',
			category: 'Travel',
			budget: 'September Budget',
			type: 'once-off'
		},
		{
			name: 'Transportation',
			price: 60.0,
			date: '25 September 2024',
			category: 'Travel',
			budget: 'September Budget',
			type: 'once-off'
		},
		{
			name: 'Transportation',
			price: 60.0,
			date: '25 September 2024',
			category: 'Travel',
			budget: 'September Budget',
			type: 'once-off'
		}
	]);
	let totalSpent = $derived(expenseItems.reduce((total, expense) => total + expense.price, 0));
	let currency = $state('R');

	let expenseCategory = $state([
		{ name: 'Utilities', id: 9 },
		{ name: 'Groceries', id: 9 },
		{ name: 'Loans', id: 9 },
		{ name: 'Important', id: 9 }
	]);

	let userBudgets = $state([
		{ name: 'December Budget', id: 9 },
		{ name: 'October Budget', id: 9 },
		{ name: 'November Budget', id: 9 },
		{ name: 'Outing Budget', id: 9 }
	]);
</script>
<!-- Mobile Widgets -->
<div class="hidden sm:show grid grid-cols-2 items-center p-2">

	<!-- Remaining balance -->
	<div
		class="items-center text-center p-2 rounded-xl shadow-md transition duration-300 bg-gray-100 glass backdrop-blur-md w-fit border-gray-600 mt-2"
	>
		<div class="p-1">
			<p class="text-md font-bold text-gray-600">Remaining balance</p>
		</div>
		<div
			class="text-2xl font-bold text-emerald-900 border-none  transition duration-500 bg-slate-200 rounded-lg p-2"
		>
			+{currency}	
			{totalSpent}
		</div>
	</div>

	<!-- Total amount Spent -->
	<div
		class="items-center text-center p-2 ml-2 rounded-xl transition duration-300 bg-gray-100 glass w-fit backdrop-blur-md  border-none shadow-md mt-2"
	>
		<div class="p-1">
			<p class="text-md font-bold text-gray-600">Total Spent</p>
		</div>
		<div
			class="text-2xl font-bold text-rose-900 transition duration-500 bg-red-100 rounded-lg p-2"
		>
			{currency}
			-{totalSpent}
		</div>
	</div>
</div>

<div class="grid lg:grid-cols-4 sm:grid-cols-2">
	{#each expenseItems as expense}
		<Card.Root class="lg:w-[90%] m-3 sm:w-[50%]">
			<Card.Header class="text-center p-1">
				<Card.Title class="text-md">{expense.name} - {expense.date}</Card.Title>

				<Card.Description>
					<span>
						<Badge class="italic text-xs shadow-sm" variant="outline">{expense.category}</Badge>
					</span>
				</Card.Description>
			</Card.Header>

			<Card.Content class="text-center p-0">
				<span><p class="my-auto text-3xl italic">{currency} {expense.price}</p></span>
			</Card.Content>

			<Card.Footer class="flex justify-between p-1.5">
				<!-- Edit expense pop up -->

				<Dialog.Root>
					<Dialog.Trigger class={buttonVariants({ variant: 'outline' })}>Edit</Dialog.Trigger>

					<Dialog.Content class="sm:max-w-[400px]">
						<Dialog.Header>
							<Dialog.Title class="text-center">{expense.name}</Dialog.Title>
						</Dialog.Header>

						<div class="grid gap-2 -py-1">
							<!-- Expense name -->
							<div class="grid grid-cols-4 items-center gap-2">
								<Label for="name" class="text-left">Name</Label>
								<Input id="name" value={expense.name} class="col-span-3 w-[260px]" />
							</div>

							<!-- Expense type -->
							<div class="grid grid-cols-4 items-center gap-2">
								<Label for="username" class="text-left">Type:</Label>

								<Select.Root>
									<Select.Trigger class="w-[260px]">
										<Select.Value placeholder={expense.category} />
									</Select.Trigger>
									<Select.Content>
										<Select.Group>
											<Select.Label>Type</Select.Label>
											{#each expenseCategory as type}
												<Select.Item value={type.id} label={type.name}>{type.name}</Select.Item>
											{/each}
										</Select.Group>
									</Select.Content>
									<Select.Input name="expense_type" />
								</Select.Root>
							</div>

							<!-- Linked budget -->
							<div class="grid grid-cols-4 items-center gap-2">
								<Label for="username" class="text-left">Budget:</Label>

								<Select.Root>
									<Select.Trigger class="w-[260px]">
										<Select.Value placeholder={expense.budget} />
									</Select.Trigger>
									<Select.Content>
										<Select.Group>
											<Select.Label>Budget</Select.Label>
											{#each userBudgets as budget}
												<Select.Item value={budget.id} label={budget.name}
													>{budget.name}</Select.Item
												>
											{/each}
										</Select.Group>
									</Select.Content>
									<Select.Input name="expense_type" />
								</Select.Root>
							</div>

							<!-- Expense amount -->
							<div class="grid grid-cols-4 items-center gap-2">
								<Label for="amount" class="text-left">Amount:</Label>
								<Input id="amount" value={expense.price} class="col-span-3" />
							</div>

							<!-- Expense date -->
							<div class="grid grid-cols-4 items-center gap-2">
								<Label for="username" class="text-left">Date</Label>
								<input type="date" />
							</div>
						</div>

						<Dialog.Footer>
							<Button type="submit" class="mx-auto">Update</Button>
						</Dialog.Footer>
					</Dialog.Content>
				</Dialog.Root>

				<Button class={buttonVariants({ variant: 'outline' })}>X</Button>
			</Card.Footer>
		</Card.Root>
	{/each}
</div>

<Dialog.Root>
	<Dialog.Trigger
		class="btn fixed bottom-4 right-4 text-white py-2 px-4 rounded-3xl hover:font-bold hover:scale-95 transition duration-200 ease-in-out sm:mb-10"
		>Add</Dialog.Trigger
	>

	<Dialog.Content class="sm:max-w-[400px]">
		<Dialog.Header>
			<Dialog.Title class="text-center">Add new expense</Dialog.Title>
		</Dialog.Header>

		<div class="grid gap-2 -py-1">
			<!-- Expense name -->
			<div class="grid grid-cols-4 items-center gap-2">
				<Label for="name" class="text-left">Name</Label>
				<Input id="name" class="col-span-3 w-[260px]" />
			</div>

			<!-- Expense type -->
			<div class="grid grid-cols-4 items-center gap-2">
				<Label for="username" class="text-left">Type:</Label>

				<Select.Root>
					<Select.Trigger class="w-[260px]">
						<Select.Value />
					</Select.Trigger>
					<Select.Content>
						<Select.Group>
							<Select.Label>Type</Select.Label>
							{#each expenseCategory as type}
								<Select.Item value={type.id} label={type.name}>{type.name}</Select.Item>
							{/each}
						</Select.Group>
					</Select.Content>
					<Select.Input name="expense_type" />
				</Select.Root>
			</div>

			<!-- Linked budget -->
			<div class="grid grid-cols-4 items-center gap-2">
				<Label for="username" class="text-left">Budget:</Label>

				<Select.Root>
					<Select.Trigger class="w-[260px]">
						<Select.Value />
					</Select.Trigger>
					<Select.Content>
						<Select.Group>
							<Select.Label>Budget</Select.Label>
							{#each userBudgets as budget}
								<Select.Item value={budget.id} label={budget.name}>{budget.name}</Select.Item>
							{/each}
						</Select.Group>
					</Select.Content>
					<Select.Input name="expense_type" />
				</Select.Root>
			</div>

			<!-- Expense amount -->
			<div class="grid grid-cols-4 items-center gap-2">
				<Label for="amount" class="text-left">Amount:</Label>
				<Input id="amount" class="col-span-3" />
			</div>

			<!-- Expense date -->
			<div class="grid grid-cols-4 items-center gap-2">
				<Label for="username" class="text-left">Date</Label>
				<DatePicker></DatePicker>
			</div>
		</div>

		<Dialog.Footer>
			<Button type="submit" class="mx-auto">Save</Button>
		</Dialog.Footer>

	</Dialog.Content>
</Dialog.Root>
