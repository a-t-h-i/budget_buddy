<script lang="ts">
import * as Tabs from "$lib/components/ui/tabs/index.js";
import * as Card from "$lib/components/ui/card/index.js";
import {
    Button
} from "$lib/components/ui/button/index.js";
import {
    Input
} from "$lib/components/ui/input/index.js";
import {
    Label
} from "$lib/components/ui/label/index.js";
import {
    toast
} from "svelte-sonner";
import {
    redirect
} from '@sveltejs/kit';

import Footer from "./partials/footer.svelte";
	import { goto } from "$app/navigation";

const moneySymbols = ['💵', '💰', '💳', '💴', '💶', '🏦', '🏧', '🤑', '💸', '🪙', '🧾', '📊', '📈', '📉', '🔍', '📅'];
let Logo = $state(moneySymbols[Math.floor(Math.random() * moneySymbols.length)]);
let userName = $state("");
let userPassword = $state("");
let correctUserDetails = $state(true);

</script>

<div class="items-center p-2 rounded-xl m-2 mt-2 lg:h-[1020px] sm:h-screen my-auto rounded-xl">
    <div class="text-center w-[21%] h-[10%] mx-auto m-2">
        <!-- Logo -->
        <h6 class="font-black text-3xl antialiased mt-10">budgetBuddy <span class="hover:scale-110 transition duration-300 ease-in-out">{Logo}</span></h6>
    </div>

    <div>

        <Tabs.Root value="account" class="w-[30%] mx-auto">
            <Tabs.List class="grid w-full grid-cols-2">
                <Tabs.Trigger value="account">Login</Tabs.Trigger>
                <Tabs.Trigger value="register">Register</Tabs.Trigger>
            </Tabs.List>

            <!-- Login tab -->
            <Tabs.Content value="account">
                <form id="userLogin">
                    <Card.Root>

                        <Card.Header class="items-center">
                            <Card.Description  hidden={!correctUserDetails}>
                                Please enter your login details to continue...
                            </Card.Description>

                            <Card.Description class="text-red-400 font-black" hidden={correctUserDetails}>
                                Incorrect password or user does not exist!
                            </Card.Description>

                        </Card.Header>

                        <Card.Content class="space-y-2">
                            <!-- Username -->
                            <div class="space-y-1">
                                <Label for="username">Username</Label>
                                <Input id="username" placeholder="Username" bind:value={userName} />
                            </div>

                            <!-- Password -->
                            <div class="space-y-1">
                                <Label for="username">Password</Label>
                                <Input id="password" type="password" bind:value={userPassword}/>
                            </div>
                        </Card.Content>

                        <Card.Footer>
                            <Button class="mx-auto w-[50%]" type="submit" form="userLogin">Login</Button>
                        </Card.Footer>
                    </Card.Root>
                </form>
            </Tabs.Content>

            <Tabs.Content value="register">
                <form method="POST" action="" id="registerNewUser">
                    <Card.Root>
                        <Card.Header class="items-center">
                            <Card.Title>Create An Account</Card.Title>
                            <Card.Description>
                                Create a new budget buddy account.
                            </Card.Description>
                        </Card.Header>

                        <Card.Content class="space-y-2">
                            <!-- Username -->
                            <div class="space-y-1">
                                <Label for="username">Username</Label>
                                <Input id="username"/>
                            </div>

                            <!-- Email -->
                            <div class="space-y-1">
                                <Label for="email">Email</Label>
                                <Input id="email" type="email"/>
                            </div>

                            <!-- New Password -->
                            <div class="space-y-1">
                                <Label for="password">New password <span class="text-red-400">*</span></Label>
                                <Input id="password" type="password" required/>
                            </div>
                            <!-- Confirm New Password -->
                            <div class="space-y-1">
                                <Label for="confim">Confirm password <span class="text-red-400">*</span></Label>
                                <Input id="confirm" type="password" />
                            </div>
                        </Card.Content>

                        <!-- Register Button -->
                        <Card.Footer>
                            <Button type="submit" class="float-center" form="registerNewUser">Register</Button>
                        </Card.Footer>

                    </Card.Root>
                </form>
            </Tabs.Content>
        </Tabs.Root>
    </div>

</div>

<footer>
    <Footer></Footer>
</footer>
