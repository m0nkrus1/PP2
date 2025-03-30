import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Drawing Tool")
    clock = pygame.time.Clock()
    
    # Drawing variables
    radius = 15
    drawing = False
    shape = 'line'
    start_pos = (0, 0)
    color = (0, 0, 255)
    points = []
    eraser_color = (0, 0, 0)
    
    # Colors palette
    colors = [
        (255, 0, 0),
        (0, 255, 0),
        (0, 0, 255),
        (255, 255, 0),
        (255, 0, 255),
        (0, 255, 255),
        (255, 255, 255),
        (0, 0, 0)
    ]
    
    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                
                # Shape selection
                if event.key == pygame.K_l:
                    shape = 'line'
                elif event.key == pygame.K_r:
                    shape = 'rectangle'
                elif event.key == pygame.K_c:
                    shape = 'circle'
                elif event.key == pygame.K_e:
                    shape = 'eraser'
                
                # Color selection with number keys
                for i in range(min(9, len(colors) + 1)):
                    if event.key == getattr(pygame, f"K_{i}"):
                        if i == 0:
                            if len(colors) > 8:
                                color = colors[8]
                        elif i - 1 < len(colors):
                            color = colors[i - 1]
            
            # Mouse events
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    drawing = True
                    start_pos = event.pos
                    if shape == 'line' or shape == 'eraser':
                        points.append(event.pos)
                elif event.button == 3:
                    if pressed[pygame.K_LSHIFT] or pressed[pygame.K_RSHIFT]:
                        radius = min(200, radius + 5)
                    else:
                        radius = max(1, radius - 5)
            
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    drawing = False
                    if shape == 'rectangle':
                        end_pos = event.pos
                        rect = pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
                        pygame.draw.rect(screen, color, rect, radius if radius < 10 else 3)
                    elif shape == 'circle':
                        end_pos = event.pos
                        dx = end_pos[0] - start_pos[0]
                        dy = end_pos[1] - start_pos[1]
                        circle_radius = max(1, int((dx**2 + dy**2)**0.5))
                        pygame.draw.circle(screen, color, start_pos, circle_radius, radius if radius < 10 else 3)
            
            if event.type == pygame.MOUSEMOTION:
                if drawing:
                    if shape == 'line' or shape == 'eraser':
                        points.append(event.pos)
                        points = points[-512:]
        
        screen.fill((0, 0, 0))
        
        # Draw color palette
        for i, c in enumerate(colors):
            pygame.draw.rect(screen, c, (10 + i*30, 10, 25, 25))
            if c == color:
                pygame.draw.rect(screen, (255, 255, 255), (10 + i*30, 10, 25, 25), 2)
        
        # Draw shape indicators
        font = pygame.font.SysFont(None, 24)
        shapes_text = font.render(f"L:Line R:Rect C:Circle E:Eraser", True, (255, 255, 255))
        screen.blit(shapes_text, (10, 40))
        
        # Draw current settings
        settings_text = font.render(f"Shape: {shape.capitalize()} | Size: {radius} | Color: {color}", True, (255, 255, 255))
        screen.blit(settings_text, (10, 70))
        
        # Draw all points for line or eraser
        if shape == 'line' or shape == 'eraser':
            i = 0
            while i < len(points) - 1:
                current_color = eraser_color if shape == 'eraser' else color
                drawLineBetween(screen, i, points[i], points[i + 1], radius, current_color)
                i += 1
        
        # Draw preview for rectangle or circle
        if drawing and (shape == 'rectangle' or shape == 'circle'):
            current_pos = pygame.mouse.get_pos()
            if shape == 'rectangle':
                rect = pygame.Rect(start_pos, (current_pos[0] - start_pos[0], current_pos[1] - start_pos[1]))
                pygame.draw.rect(screen, color, rect, 1)
            elif shape == 'circle':
                dx = current_pos[0] - start_pos[0]
                dy = current_pos[1] - start_pos[1]
                circle_radius = max(1, int((dx**2 + dy**2)**0.5))
                pygame.draw.circle(screen, color, start_pos, circle_radius, 1)
        
        pygame.display.flip()
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color):
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

if __name__ == "__main__":
    main()
