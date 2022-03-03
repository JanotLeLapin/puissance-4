import { Socket } from "socket.io";

export class Room {
    private _board: number[][] = [
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1],
    ];
    private _players: Socket[];
    private _turn: number = 0;

    constructor(players: Socket[]) {
        this._players = players;
    }

    playerMove(player: Socket, col: number): void {
        for (let i = 5; i > 0; i--) {
            if (this._board[i][col] === -1) {
                this._board[i][col] = this._players.indexOf(player);
                break;
            }
        }

        this._players.forEach((player) => player.emit("board", this._board));
    }

    private checkHorizontal(): number {
        for (let i = 0; i < 6; i++) {
            for (let j = 0; j < 4; j++) {
                if (
                    this._board[i][j] !== -1 &&
                    this._board[i][j] === this._board[i][j + 1] &&
                    this._board[i][j] === this._board[i][j + 2] &&
                    this._board[i][j] === this._board[i][j + 3]
                ) {
                    return this._board[i][j];
                }
            }
        }
        return -1;
    }

    private checkVertical(): number {
        for (let i = 0; i < 3; i++) {
            for (let j = 0; j < 6; j++) {
                if (
                    this._board[i][j] !== -1 &&
                    this._board[i][j] === this._board[i + 1][j] &&
                    this._board[i][j] === this._board[i + 2][j] &&
                    this._board[i][j] === this._board[i + 3][j]
                ) {
                    return this._board[i][j];
                }
            }
        }
        return -1;
    }

    private checkDiagonalLeft(): number {
        for (let i = 0; i < 3; i++) {
            for (let j = 0; j < 4; j++) {
                if (
                    this._board[i][j] !== -1 &&
                    this._board[i][j] === this._board[i + 1][j + 1] &&
                    this._board[i][j] === this._board[i + 2][j + 2] &&
                    this._board[i][j] === this._board[i + 3][j + 3]
                ) {
                    return this._board[i][j];
                }
            }
        }
        return -1;
    }

    private checkDiagonalRight(): number {
        for (let i = 3; i < 6; i++) {
            for (let j = 0; j < 4; j++) {
                if (
                    this._board[i][j] !== -1 &&
                    this._board[i][j] === this._board[i - 1][j + 1] &&
                    this._board[i][j] === this._board[i - 2][j + 2] &&
                    this._board[i][j] === this._board[i - 3][j + 3]
                ) {
                    return this._board[i][j];
                }
            }
        }
        return -1;
    }

    checkWin() {
        return Math.max(
            this.checkHorizontal(),
            this.checkVertical(),
            this.checkDiagonalLeft(),
            this.checkDiagonalRight()
        );
    }

    get board(): number[][] {
        return this._board;
    }

    get players(): Socket[] {
        return this._players;
    }

    get turn(): Socket {
        return this._players[this._turn];
    }

    set turn(turn: Socket) {
        this._turn = this._players.indexOf(turn);
    }
}
