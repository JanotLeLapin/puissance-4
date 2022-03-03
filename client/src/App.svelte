<script lang="ts">
    import { io } from "socket.io-client";

    export let host: string;

    export let board: number[][] = [
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1],
    ];

    export let waiting = false;
    export let play = false;

    export let win = false;
    export let lose = false;

    export const socket = io(host);

    socket.on("wait", () => (waiting = true));
    socket.on("start", () => (waiting = false));
    socket.on("play", (data: any) => (play = data === socket.id));
    socket.on("board", (data: number[][]) => (board = data));
    socket.on("win", () => (win = true));
    socket.on("lose", () => (lose = true));
</script>

<main>
    <div class={`title ${win || lose ? "show-title" : ""}`}>
        <h1>{win ? "Vous avez gagné !" : "Vous avez perdu !"}</h1>
    </div>

    <div class={win || lose ? "blur" : ""}>
        <h1>Puissance 4 du Prestige</h1>

        {#each board as line}
            <div class="line">
                {#each line as token}
                    <div
                        class={`token ${
                            token == -1
                                ? "hidden"
                                : token == 0
                                ? "yellow"
                                : "red"
                        }`}
                    />
                {/each}
            </div>
        {/each}
        <div class="line">
            {#each [...Array(7).keys()] as i}
                <button
                    disabled={board[0][i] != -1 ||
                        waiting ||
                        !play ||
                        win ||
                        lose}
                    on:click={() => {
                        socket.emit("play", i);
                    }}
                >
                    {i + 1}
                </button>
            {/each}
        </div>

        {#if !win && !lose}
            {#if waiting}
                <p>En attente d'un adversaire...</p>
            {/if}

            {#if !play && !waiting}
                <p>Tour de l'adversaire</p>
            {/if}
        {/if}
    </div>
</main>

<style>
    :root {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
            Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
    }

    main {
        --size: 64px;
        text-align: center;
        margin: 0 auto;
    }

    .line {
        display: flex;
        justify-content: center;
    }

    .token,
    button {
        width: var(--size);
        margin: 4px;
    }

    .token {
        border-radius: var(--size);
        height: var(--size);
    }

    button {
        border-radius: 999px;
        font-weight: bold;
        color: white;
        border: none;
        background-color: #0ea5e9;
        padding: 0.2rem;
        transition: 150ms ease-in-out;
    }

    button:disabled {
        background-color: #ef4444;
    }

    button:enabled:hover {
        background-color: #7dd3fc;
    }

    .yellow {
        background-color: #fbbf24;
    }

    .red {
        background-color: #ef4444;
    }

    .yellow,
    .red {
        animation-name: drop;
        animation-duration: 200ms;
    }

    .hidden {
        opacity: 0;
    }

    .title {
        z-index: 99;
        font-size: xx-large;
        position: absolute;
        left: 0;
        right: 0;
        margin-left: auto;
        margin-right: auto;
        width: 400px;
        transform: translateY(-400px);
    }

    .show-title {
        animation-name: show-title;
        animation-duration: 500ms;
        transform: translateY(200px);
    }

    .blur {
        filter: blur(15px);
        transition: 200ms ease-in-out;
    }

    @keyframes drop {
        0% {
            transform: translateY(-800px);
        }
        50% {
            transform: translateY(0px);
        }
        80% {
            transform: translateY(-15px);
        }
        100% {
            transform: translateY(0px);
        }
    }

    @keyframes show-title {
        0% {
            transform: translateY(-300px);
        }
        75% {
            transform: translateY(210px);
        }
        100% {
            transform: translateY(200px);
        }
    }
</style>
