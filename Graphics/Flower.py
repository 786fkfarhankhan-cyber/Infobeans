

import pygame
import math
import sys

pygame.init()

WIDTH, HEIGHT = 900, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("A Rose Comes to Life")

clock = pygame.time.Clock()

# Colors
SKY = (18, 35, 34)
GROUND = (24, 48, 32)
STEM = (35, 110, 48)
LEAF = (35, 125, 55)
DARK_LEAF = (20, 75, 35)
RED = (190, 20, 45)
DARK_RED = (105, 8, 28)
PINK = (245, 75, 100)

# Animation timer
start_time = pygame.time.get_ticks()


def get_progress(seconds, duration):
    return max(0, min(1, seconds / duration))


def bezier(p0, p1, p2, p3, t):
    x = ((1-t)**3*p0[0] +
         3*(1-t)**2*t*p1[0] +
         3*(1-t)*t**2*p2[0] +
         t**3*p3[0])

    y = ((1-t)**3*p0[1] +
         3*(1-t)**2*t*p1[1] +
         3*(1-t)*t**2*p2[1] +
         t**3*p3[1])

    return (int(x), int(y))


def draw_background():
    screen.fill(SKY)

    # Ground
    pygame.draw.rect(screen, GROUND, (0, 620, WIDTH, 80))

    # Soft horizon glow
    for radius in range(180, 0, -5):
        alpha = radius / 180
        color = (
            int(25 + 15 * alpha),
            int(55 + 20 * alpha),
            int(38 + 10 * alpha)
        )

        pygame.draw.circle(
            screen, color, (450, 400), radius
        )


def draw_stem(progress):
    points = []

    p0 = (440, 630)
    p1 = (390, 500)
    p2 = (500, 350)
    p3 = (420, 220)

    for i in range(101):
        t = i / 100

        if t > progress:
            break

        points.append(bezier(p0, p1, p2, p3, t))

    if len(points) > 1:
        pygame.draw.lines(screen, DARK_LEAF, False, points, 12)
        pygame.draw.lines(screen, STEM, False, points, 7)

    return points


def draw_leaf(x, y, angle, progress):
    if progress <= 0:
        return

    length = int(90 * progress)
    width = int(35 * progress)

    if length < 2:
        return

    # Leaf surface
    leaf = pygame.Surface((length + 30, width * 2 + 30), pygame.SRCALPHA)

    center_y = width + 15

    # Pointed leaf shape
    points = [
        (10, center_y),
        (length // 3, center_y - width),
        (length, center_y - 4),
        (length // 2, center_y + width),
        (10, center_y)
    ]

    pygame.draw.polygon(leaf, LEAF, points)
    pygame.draw.lines(leaf, DARK_LEAF, False, points, 2)

    # Leaf vein
    pygame.draw.line(
        leaf, (125, 170, 75),
        (10, center_y),
        (length, center_y - 4), 2
    )

    # Side veins
    for i in range(1, 5):
        vx = int(length * i / 5)
        pygame.draw.line(
            leaf, DARK_LEAF,
            (vx, center_y - 3),
            (vx - 10, center_y - width // 2), 1
        )
        pygame.draw.line(
            leaf, DARK_LEAF,
            (vx, center_y - 3),
            (vx - 10, center_y + width // 2), 1
        )

    rotated = pygame.transform.rotate(leaf, angle)

    screen.blit(
        rotated,
        rotated.get_rect(center=(x, y))
    )


def draw_petal(x, y, width, height, color, angle):
    # Draw one soft, rounded petal
    petal = pygame.Surface(
        (width * 2 + 20, height * 2 + 20),
        pygame.SRCALPHA
    )

    cx = width + 10
    cy = height + 10

    # Petal body
    pygame.draw.ellipse(
        petal,
        color,
        (cx - width // 2, cy - height // 2,
         width, height)
    )

    # Soft highlight
    highlight = (
        min(255, color[0] + 35),
        min(255, color[1] + 25),
        min(255, color[2] + 30),
        150
    )

    pygame.draw.ellipse(
        petal,
        highlight,
        (cx - width // 4, cy - height // 3,
         width // 3, height // 2)
    )

    rotated = pygame.transform.rotate(petal, angle)

    screen.blit(
        rotated,
        rotated.get_rect(center=(x, y))
    )


def draw_rose(center_x, center_y, bloom):
    # Sepals beneath flower
    if bloom < 0.15:
        bud_size = 10 + int(bloom * 80)

        pygame.draw.ellipse(
            screen, (35, 110, 45),
            (center_x - bud_size // 2,
             center_y - bud_size,
             bud_size, bud_size * 2)
        )

        return

    # Outer petals
    outer_size = int(45 * bloom)

    for i in range(5):
        angle = i * 72

        radians = math.radians(angle)

        x = center_x + math.cos(radians) * outer_size * 0.55
        y = center_y + math.sin(radians) * outer_size * 0.35

        draw_petal(
            int(x), int(y),
            65, 85,
            (155, 15, 42),
            -angle
        )

    # Middle petals
    for i in range(6):
        angle = i * 60

        radians = math.radians(angle)

        x = center_x + math.cos(radians) * 18 * bloom
        y = center_y + math.sin(radians) * 12 * bloom

        draw_petal(
            int(x), int(y),
            48, 65,
            (205, 25, 55),
            -angle
        )

    # Inner petals
    for i in range(5):
        angle = i * 72

        radians = math.radians(angle)

        x = center_x + math.cos(radians) * 8
        y = center_y + math.sin(radians) * 7

        draw_petal(
            int(x), int(y),
            30, 43,
            (240, 65, 85),
            -angle
        )

    # Center
    pygame.draw.circle(
        screen, (115, 8, 30),
        (center_x, center_y), 12
    )


# Main animation loop
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    elapsed = (pygame.time.get_ticks() - start_time) / 1000

    draw_background()

    # Phase 1: Stem grows
    stem_progress = get_progress(elapsed, 5)

    points = draw_stem(stem_progress)

    # Phase 2: Leaves grow
    leaf_progress = get_progress(elapsed - 4, 3)

    if leaf_progress > 0:
        draw_leaf(410, 480, 25, leaf_progress)

    if leaf_progress > 0.3:
        draw_leaf(460, 390, 155, leaf_progress)

    # Phase 3: Bud grows
    bud_progress = get_progress(elapsed - 7, 3)

    # Phase 4: Flower blooms
    bloom_progress = get_progress(elapsed - 10, 6)

    flower_x = 420
    flower_y = 220

    if elapsed > 7:
        draw_rose(
            flower_x,
            flower_y,
            bloom_progress
        )

    # Small ground details
    pygame.draw.line(
        screen, (55, 90, 40),
        (300, 630), (570, 630), 3
    )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()


