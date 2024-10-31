<script lang="ts">
import {
    Button
} from "$lib/components/ui/button/index.js";
import * as Card from "$lib/components/ui/card/index.js";
import {
    Badge
} from "$lib/components/ui/badge/index.js";
import * as Popover from "$lib/components/ui/popover/index.js";
import {
    Label
} from "$lib/components/ui/label/index.js";
import {
    Input
} from "$lib/components/ui/input/index.js";
import Calendar from "$lib/components/ui/calendar/calendar.svelte";
import {
    Description
} from "formsnap";

let expenseItems = $state([{
        "name": "Groceries",
        "price": "150",
        "date": "01 September 2024",
        "category": "Food"
    },
    {
        "name": "Electricity",
        "price": "200",
        "date": "03 September 2024",
        "category": "Utilities"
    },
    {
        "name": "Internet",
        "price": "100",
        "date": "05 September 2024",
        "category": "Utilities"
    }
]);
</script>

<div class="items-center">

    <div>
        
    </div>

    <div class="grid lg:grid-cols-4 sm:grid-cols-2 overflow-y-scroll">
        {#each expenseItems as expense}
        <Card.Root class="w-[90%] m-3">

            <Card.Header class="text-center p-1">
                <Card.Title class="text-lg">{expense.name}</Card.Title>

                <Card.Description>
                    <span><Badge class="italic text-xs shadow-sm" variant="outline">{expense.category}</Badge></span>
                </Card.Description>

            </Card.Header>

            <Card.Content class="text-center p-0">
                <span><p class="my-auto text-3xl italic">ZAR {expense.price}</p></span>
            </Card.Content>

            <Card.Footer class="flex justify-between p-1.5">

                <Popover.Root>
                    <!-- Edit expense -->
                    <Popover.Trigger asChild let:builder>
                        <Button builders={[builder]} variant="outline">Edit</Button>
                    </Popover.Trigger>

                    <Popover.Content class="w-80">
                        <div class="grid gap-4">
                            <div class="space-y-2 text-center">
                                <h4 class="font-medium leading-none">{expense.name}</h4>
                                <p class="text-muted-foreground text-sm">
                                    Update expense...
                                </p>
                            </div>

                            <div class="grid gap-2">
                                <div class="grid grid-cols-3 items-center gap-4">
                                    <Label for="width">Name</Label>
                                    <Input id="width" value="{expense.name}" class="col-span-2 h-8" />
                                </div>
        
                                <div class="grid grid-cols-3 items-center gap-4">
                                    <Label for="maxWidth">Budget</Label>
                                    <Input id="maxWidth" value="{expense.category}" class="col-span-2 h-8" />
                                </div>
        
                                <div class="grid grid-cols-3 items-center gap-4">
                                    <Label for="maxWidth">Category</Label>
                                    <Input id="maxWidth" value="{expense.category}" class="col-span-2 h-8" />
                                </div>
                                <div class="grid grid-cols-3 items-center gap-4">
                                    <Label for="height">Amount</Label>
                                    <Input id="height" value="{expense.price}" class="col-span-2 h-8" />
                                </div>
                                <div class="grid grid-cols-3 items-center gap-4">
                                    <Label for="maxHeight">Date</Label>
                                    <Input id="maxHeight" value="{expense.date}" class="col-span-2 h-8" />
                                </div>

                                <div>
                                    <button class="w-[40%] btn btn-sm bg-orange-200 text-black border-none hover:bg-orange-300 hover:border-none hover:text-black float-end">Save</button>
                                </div>
                            </div>
                        </div>
                    </Popover.Content>
                </Popover.Root>

                <button class="btn btn-sm bg-orange-200 text-black border-none hover:bg-orange-300 hover:border-none hover:text-black">X</button>
            </Card.Footer>

        </Card.Root>
        {/each}
    </div>

</div>
