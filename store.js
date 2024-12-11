import { writable } from 'svelte/store';
export const isLoggedIn = writable(false);
export const token = writable(null);
export const user = writable(null);
