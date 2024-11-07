<script lang="ts">
import * as Tabs from "$lib/components/ui/tabs/index.js";
// Partials
import Home from "./partials/home.svelte";
import Footer from "../partials/footer.svelte";
import Expenses from "./partials/expenses.svelte";
import Analytics from "./partials/analytics.svelte";
import Budget from "./partials/budget.svelte";
import { cn } from "$lib/utils"
import { ScrollArea } from "$lib/components/ui/scroll-area/index.js";
import ProfileMenu from "./partials/profile_menu.svelte";

</script>

<div class="p-1 bg-neutral-100 aspect-auto">

    <div>
        <Tabs.Root value="home" class="mx-auto">
            <div class="flex flex-col-reverse sm:flex-col">
        
                <!-- Tabs List, sticky at the bottom on mobile, top on desktop -->
                <Tabs.List class="z-10 grid lg:w-fit grid-cols-5 h-fit rounded-2xl mx-auto bg-glass border shadow-lg sticky bottom-0 sm:bottom-0">
                    <Tabs.Trigger value="home" class="p-2 mr-1 hover:bg-gray-100 rounded-xl transition duration-500 ease-in-out {cn('data-[state=active]:bg-gray-200 data-[state=active]:text-gray-500 data-[state=active]:font-black data-[state=active]:border')}">
                        Home
                    </Tabs.Trigger>
                    <Tabs.Trigger value="expenses" class="p-2 mr-1 hover:bg-gray-100 rounded-xl transition duration-500 ease-in-out {cn('data-[state=active]:bg-gray-200 data-[state=active]:text-gray-500 data-[state=active]:font-black data-[state=active]:border')}">
                        Expenses
                    </Tabs.Trigger>
                    <Tabs.Trigger value="analytics" class="p-2 mr-1 hover:bg-gray-100 rounded-xl transition duration-500 ease-in-out {cn('data-[state=active]:bg-gray-200 data-[state=active]:text-gray-500 data-[state=active]:font-black data-[state=active]:border')}">
                        Analytics
                    </Tabs.Trigger>
                    <Tabs.Trigger value="budget" class="p-2 mr-1 hover:bg-gray-100 rounded-xl transition duration-500 ease-in-out {cn('data-[state=active]:bg-gray-200 data-[state=active]:text-gray-500 data-[state=active]:font-black data-[state=active]:border')}">
                        Budget
                    </Tabs.Trigger>
        
                    <!-- Profile dropdown -->
                    <ProfileMenu></ProfileMenu>
                </Tabs.List>
        
                <!-- Tabs Content -->
                <Tabs.Content value="home">
                    <ScrollArea class="sm:h-screen sm:w-full lg:h-[46vw] rounded-xl border">
                        <Home></Home>
                    </ScrollArea>
                </Tabs.Content>
        
                <Tabs.Content value="expenses">
                    <Expenses></Expenses>
                </Tabs.Content>
        
                <Tabs.Content value="analytics">
                    <ScrollArea class="sm:h-screen sm:w-full lg:h-[46vw] rounded-xl border">
                        <Analytics></Analytics>
                    </ScrollArea>
                </Tabs.Content>
        
                <Tabs.Content value="budget">
                    <ScrollArea class="sm:h-screen sm:w-full lg:h-[46vw] rounded-xl border">
                        <Budget></Budget>
                    </ScrollArea>
                </Tabs.Content>
        
            </div>
        </Tabs.Root>
        
    </div>

</div>
<footer>
    <Footer></Footer>
</footer>
