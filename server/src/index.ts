import express from "express";
import cors from "cors";
import path from "path";
import { createServer } from "http";
import { Server, Socket } from "socket.io";
import { Room } from "./room";

const app = express();
const server = createServer(app);

app.use(cors());

app.use(express.static(path.join(process.cwd(), "..", "client", "dist")));
app.use((_req, res) => {
    res.sendFile(
        path.join(process.cwd(), "..", "client", "dist", "index.html")
    );
});

const io = new Server(server, {
    cors: {
        origin: "*",
    },
});

const rooms: Room[] = [];

let temp: Socket | undefined;

io.on("connection", (socket) => {
    if (temp) {
        const room = new Room([temp, socket]);
        rooms.push(room);

        room.players.forEach((player) => {
            player.emit("start");
            player.emit("play", room.turn.id);

            player.on("play", (col) => {
                if (room.turn.id === player.id) {
                    room.playerMove(player, col);
                    room.turn = room.players.find(
                        (p) => p !== player
                    ) as Socket;

                    room.players.forEach((player) => {
                        player.emit("board", room.board);
                        player.emit("play", room.turn.id);
                    });

                    const win = room.checkWin();
                    if (win !== -1) {
                        room.players[win].emit("win");
                        room.players[(win + 1) % 2].emit("lose");

                        rooms.splice(rooms.indexOf(room), 1);
                    }
                }
            });
        });

        temp = undefined;
    } else {
        temp = socket;
        temp.emit("wait");
    }
});

server.listen(5000);
