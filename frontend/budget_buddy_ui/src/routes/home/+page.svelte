<script lang="ts">
import * as Tabs from "$lib/components/ui/tabs/index.js";
import * as Avatar from "$lib/components/ui/avatar";
import * as Menubar from "$lib/components/ui/menubar/index.js";


// Partials
import Home from "./partials/home.svelte";
import Footer from "../partials/footer.svelte";
import Expenses from "./partials/expenses.svelte";
import Analytics from "./partials/analytics.svelte";
import Budget from "./partials/budget.svelte";
import Goals from "./partials/goals.svelte";
import { ScrollArea } from "$lib/components/ui/scroll-area/index.js";

const users = $state([{
    id: 1,
    name: "Steve"
}, {
    id: 2,
    name: "Eve"
}, {
    id: 3,
    name: "Jack"
}, {
    id: 4,
    name: "Joe"
}]);
let hideFooter = $state(false);
const userId = $state(1);

function removeFooter(){
    hideFooter = !hideFooter;
};


</script>

<div class="rounded-xl p-1 lg:h-full sm:h-screen">

    <div>

        <Tabs.Root value="account" class="lg:w-1200px mx-auto">
            <Tabs.List class="grid w-full grid-cols-6 h-fit rounded-xl bg-inherit border">
                <Tabs.Trigger value="home" class="p-2 font-black rounded-xl hover:shadow-md hover:border transition duration-300 ease-in-out">Home</Tabs.Trigger>
                <Tabs.Trigger value="expenses" class="p-2 font-black rounded-xl hover:shadow-md hover:border transition duration-300 ease-in-out">Expenses</Tabs.Trigger>
                <Tabs.Trigger value="analytics" class="p-2 font-black rounded-xl hover:shadow-md hover:border transition duration-300 ease-in-out">Analytics</Tabs.Trigger>
                <Tabs.Trigger value="budget" class="p-2 font-black rounded-xl hover:shadow-md hover:border transition duration-300 ease-in-out">Budget</Tabs.Trigger>
                <Tabs.Trigger value="goals" class="p-2 font-black rounded-xl hover:shadow-md hover:border transition duration-300 ease-in-out">Goals</Tabs.Trigger>

                <Menubar.Root class="shadow-none border-none bg-inherit w-[10%]">
                    <Menubar.Menu>
                        <Menubar.Trigger>
                            <Avatar.Root class="rounded-md">
                                <Avatar.Image src="https://github.com/shadcn.png" alt="@shadcn" />
                                <Avatar.Fallback>User</Avatar.Fallback>
                            </Avatar.Root>
                        </Menubar.Trigger>

                        <Menubar.Content class="">
                            <Menubar.Menu>
                                <Menubar.Item class="hover:border rounded-md transition duration-300 ease-in-out">
                                    Profile
                                </Menubar.Item>

                                <Menubar.Item on:click={removeFooter} class="hover:border rounded-md transition duration-300 ease-in-out">
                                    Log Out
                                </Menubar.Item>
                            </Menubar.Menu>
                        </Menubar.Content>
                        
                    </Menubar.Menu>
                </Menubar.Root>

            </Tabs.List>

            <!-- Home tab -->
            <Tabs.Content value="home">
                <ScrollArea class="sm:h-screen sm:w-full lg:h-[46vw] rounded-xl border">
                    <Home></Home>
                </ScrollArea>
            </Tabs.Content>

            <!-- Expenses tab -->
            <Tabs.Content value="expenses">
                <ScrollArea class="sm:h-screen sm:w-full lg:h-[46vw] rounded-xl border">
                    <Expenses></Expenses>
                </ScrollArea>
            </Tabs.Content>

            <!-- Analytics tab -->
            <Tabs.Content value="analytics">
                <ScrollArea class="sm:h-screen sm:w-full lg:h-[46vw] rounded-xl border">
                    <Analytics></Analytics>
                </ScrollArea>
            </Tabs.Content>

            <!-- Budget tab -->
            <Tabs.Content value="budget">
                <ScrollArea class="sm:h-screen sm:w-full lg:h-[46vw] rounded-xl border">
                    <Budget></Budget>
                </ScrollArea>
            </Tabs.Content>

            <!-- Goals tab -->
            <Tabs.Content value="goals">
                <ScrollArea class="sm:h-screen sm:w-full lg:h-[46vw] rounded-xl border">
                    <Goals></Goals>
                </ScrollArea>
            </Tabs.Content>

        </Tabs.Root>
    </div>

</div>
<footer hidden={hideFooter}>
    <Footer></Footer>
</footer>
