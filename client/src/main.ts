import App from "./App.svelte";

const app = new App({
    target: document.getElementById("app"),
    props: {
        // Laissez tel quel si vous voulez jouer en local
        // Remplacez par votre adresse IP et ouvrez le port 5000 de votre routeur pour jouer en ligne
        host: "http://127.0.0.1:5000/",
    },
});

export default app;
