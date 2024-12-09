import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'

export default defineConfig({
  base: '/smv/',
  plugins: [svelte()],
  server: {
    open:true,
    historyApiFallback: true,
    port: 5173, // Ensure it's set to 5173
  },
})
