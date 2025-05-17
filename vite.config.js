import { defineConfig } from 'vite'


export default defineConfig({
    build: {
        outDir: 'static/dist',
        rollupOptions: {
            input: 'static/main.js',
            output: {
                entryFileNames: 'bundle.js'
            }
        },
        emptyOutDir: false
    }
})