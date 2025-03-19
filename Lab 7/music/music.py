import pygame

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((800, 480))

COLOR_WHITE = (255, 255, 255)

_songs = ['candy.mp3', 'low_tide.mp3', 'runaway_kid.mp3']

def next_song():
    global _songs
    _songs = _songs[1:] + [_songs[0]]
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play()

def previous_song():
    global _songs
    _songs = [_songs[-1]] + _songs[:-1]
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play()

paused = False

def stopping():
    global paused
    paused = not paused
    if paused:
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()

clock = pygame.time.Clock()
FPS = 60

SONG_END = pygame.USEREVENT + 1 
pygame.mixer.music.set_endevent(SONG_END)

pygame.mixer.music.load(_songs[0])
pygame.mixer.music.play()

running = True
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                next_song()
            if event.key == pygame.K_LEFT:
                previous_song()
            if event.key == pygame.K_SPACE:
                stopping()
        if event.type == SONG_END:
            next_song()

    screen.fill(COLOR_WHITE)

    pygame.display.flip()
    clock.tick(FPS)
