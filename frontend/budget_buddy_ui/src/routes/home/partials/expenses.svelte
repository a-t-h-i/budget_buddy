<script lang="ts">
	import { Button } from '$lib/components/ui/button/index.js';
	import * as Card from '$lib/components/ui/card/index.js';
	import { Badge } from '$lib/components/ui/badge/index.js';
	import { buttonVariants } from '$lib/components/ui/button/index.js';
	import * as Dialog from '$lib/components/ui/dialog/index.js';
	import { Input } from '$lib/components/ui/input/index.js';
	import { Label } from '$lib/components/ui/label/index.js';
	import * as Select from '$lib/components/ui/select/index.js';

	let expenseItems = $state([
		{
			name: 'Groceries',
			price: '150',
			date: '01 September 2024',
			category: 'Food',
            budget: 'December Budget'
		},
		{
			name: 'Electricity',
			price: '200',
			date: '03 September 2024',
			category: 'Utilities',
            budget: 'October Budget'
		},
		{
			name: 'Internet',
			price: '100',
			date: '05 September 2024',
			category: 'Utilities',
            budget: 'November Budget'
		}
	]);

    let currency = $state("R");

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

<div class="items-center overflow-y-scroll lg:h-screen">
	<div class="grid lg:grid-cols-4 sm:grid-cols-2">
		{#each expenseItems as expense}
			<Card.Root class="lg:w-[90%] m-3 sm:w-[50%]">
				<Card.Header class="text-center p-1">
					<Card.Title class="text-md">{expense.name} - {expense.date}</Card.Title>

					<Card.Description>
						<span><Badge class="italic text-xs shadow-sm" variant="outline">{expense.category}</Badge
							></span
						>
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
										<Label for="username" class="text-left">Type: </Label>

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
										<Label for="username" class="text-left">Budget: </Label>

										<Select.Root>
											<Select.Trigger class="w-[260px]">
												<Select.Value placeholder={expense.budget} />
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
										<Label for="amount" class="text-left">Amount: </Label>
										<Input id="amount" value={expense.price} class="col-span-3"/>
									</div>

                                    <!-- Expense date -->
									<div class="grid grid-cols-4 items-center gap-2">
										<Label for="username" class="text-left">Date</Label>
										<input type="date">
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

</div>
