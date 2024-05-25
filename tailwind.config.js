/** @type {import('tailwindcss').Config} */
module.exports = {
	content: ["./budget_buddy/templates/**/*.{html,js}", "./budget_buddy/templates/**/*.{html,js}"],
	theme: {
		extend: {},
	},
	plugins: [require("daisyui")],
	daisyui: {
		themes: ["light", "dark"],
	},
};
