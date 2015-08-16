#include <stdio.h>
#include <stdbool.h>

void room_msg(int x);
void help_msg(void);

int main(void)
{
	int room = 0;
	int game_loop = 1;

	help_msg();
	room_msg(room);
	while (game_loop) {
		switch (getchar()) {
		case 'h':
			room--;
			room_msg(room);
			break;
		case 'l':
			room++;
			room_msg(room);
			break;
		case '?': help_msg(); break;
		case 'q': game_loop = 0; break;
		default: break;
		}
	}

	printf("thanks for playing\n");

	return 0;
}

void room_msg(int x)
{
	printf("you are in room %d\n", x);
}

void help_msg(void)
{
	printf("'h' go left\n");
	printf("'l' go right\n");
	printf("'?' this help message\n");
	printf("'q' quit\n");
}
