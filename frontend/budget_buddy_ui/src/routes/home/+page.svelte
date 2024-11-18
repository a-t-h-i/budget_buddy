<script lang="ts">
import * as Tabs from "$lib/components/ui/tabs/index.js";
// Partials
import Home from "./partials/home.svelte";
import Expenses from "./partials/expenses.svelte";
import Budget from "./partials/budget.svelte";
import { cn } from "$lib/utils"
import { ScrollArea } from "$lib/components/ui/scroll-area/index.js";
import HomeIcon from "./partials/icons/home_icon.svelte";
import BudgetIcon from "./partials/icons/budget_icon.svelte";
import ExpensesIcon from "./partials/icons/expenses_icon.svelte";


</script>

<Tabs.Root value="home" class="mx-auto">
        <!-- Tabs List, sticky at the bottom on mobile, top on desktop -->
        <Tabs.List class="z-10 grid grid-cols-3 h-fit  rounded-2xl m-2 mx-auto bg-glass backdrop-blur-sm border shadow-lg sticky top-0 bottom-auto items-center w-fit">
            <Tabs.Trigger value="home" class="hover:bg-gray-100 rounded-xl transition duration-500 ease-in-out w-[100%] {cn('data-[state=active]:bg-gray-200 data-[state=active]:text-gray-500 data-[state=active]:font-black data-[state=active]:border')}">
                
                <div class="grid grid-cols-1">
                    <span class="mx-auto"><HomeIcon /></span>
                    <p>Home</p>
                </div>
                
            </Tabs.Trigger>

            <Tabs.Trigger value="expenses" class="mr-1 hover:bg-gray-100 rounded-xl transition duration-500 ease-in-out w-[100%] {cn('data-[state=active]:bg-gray-200 data-[state=active]:text-gray-500 data-[state=active]:font-black data-[state=active]:border')}">
                <div class="grid grid-cols-1">
                    <span class="mx-auto"><ExpensesIcon/></span>
                    <p>Expenses</p>
                </div>
            </Tabs.Trigger>

            <Tabs.Trigger value="budget" class="mr-1 hover:bg-gray-100 rounded-xl transition duration-500 ease-in-out w-fit w-[100%] {cn('data-[state=active]:bg-gray-200 data-[state=active]:text-gray-500 data-[state=active]:font-black data-[state=active]:border')}">
                <div class="grid grid-cols-1">
                    <span class="mx-auto"><BudgetIcon/></span>
                    <p>Budget</p>
                </div>
            </Tabs.Trigger>

        </Tabs.List>
        

        <ScrollArea class="sm:h-screen w-full lg:h-[46vw] m-1">
            <!-- Tabs Content -->
            <Tabs.Content value="home">
                    <Home />
            </Tabs.Content>
            
            <Tabs.Content value="expenses" class="sm:h-screen w-full lg:h-[46vw] m-1">
                    <Expenses />
            </Tabs.Content>

            <Tabs.Content value="budget" class="sm:h-screen w-full lg:h-[46vw] m-1">
                    <Budget />
            </Tabs.Content>
        </ScrollArea>
</Tabs.Root>
