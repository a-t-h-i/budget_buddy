<script>
	import { Footer } from "$lib/components/ui/alert-dialog";
    let year = $state(new Date().getFullYear());
</script>

<Footer class="bg-gray-100 rounded-md p-2 m-2">
    <footer class="mx-auto font-black">© Budget Buddy {year}</footer>
</Footer>