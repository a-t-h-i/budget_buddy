<script>
	import { Footer } from "$lib/components/ui/alert-dialog";
    let year = $state(new Date().getFullYear());
</script>

<Footer class="bg-neutral-100 bottom-0">
    <footer class="mx-auto">© Budget Buddy {year}</footer>
</Footer>