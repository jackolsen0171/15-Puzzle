from utils import *
import random
from PIL import Image 

from tabulate import tabulate

# table = [["Sun",696000,1989100000],["Earth",6371,5973.6],
#      ["Moon",1737,73.5],["Mars",3390,641.85]]
# print(tabulate(table))


img = Image.open("test.png")
img_width, img_height = img.size

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

def save_img(grid):
  count = 1
  for i in range(len(grid)):
    for j in range(len(grid)):
      left = i*PIXEL_SIZE
      right = left + PIXEL_SIZE
      top = j*PIXEL_SIZE
      bottom = top + PIXEL_SIZE
      crop =  img.crop((top,left,bottom,right))
      if not count > 15:
        crop.save(f'test{count}.png')
        count += 1

def draw_img(grid):
  
  count = 1
  for i in range(len(grid)):
    for j in range(len(grid)):
      a = grid[i][j]
      if not count > 15:
        img = pygame.image.load(f'test{count}.png')
        screen.blit(img,(a.newX,a.newY))
        count += 1
 
  

def welcomeScreen():
  screen.fill(BLACK)
  font = get_font(50)
  txt = font.render('15-Puzzle!',True,WHITE)
  screen.blit(txt,(128,50))
  font = get_font(30)
  txt2 = font.render('Hit spacebar to start a new game',True,WHITE)
  screen.blit(txt2,(25,150))
  # img = pygame.image.load("test.png")
  # screen.blit(img,(0,0))
  # image = pygame.image.load(r'C:\Users\user\Pictures\geek.jpg')

def won(grid):
  count = 0
  for i in range(len(grid)):
    for j in range(len(grid)):
      if grid[i][j].newX == initialGrid[i][j].x and grid[i][j].newY == initialGrid[i][j].y:
        count += 1
  if count == 16:
    return True

def shuffle(grid):
  positions = [(0,0),(128,0),(256,0),(384,0),(0,128),(128,128),(256,128),(384,128),(0,256),(128,256),(256,256),(384,256),(0,384),(128,384),(256,384),(384,384)]
  for i in range(len(grid)):
    for j in range(len(grid)):
      newPosIndex = random.randint(0,len(positions)-1)
      newPos = positions[newPosIndex]
      thisPiece = grid[i][j]
      thisPiece.newX,thisPiece.newY = newPos[0],newPos[1]

      positions.pop(newPosIndex)
  

  return grid 

  

def moveToEmpty(pos,grid):
  row = pos[1]//PIXEL_SIZE
  col = pos[0]//PIXEL_SIZE
  neighbours = [(row+1,col),(row-1,col),(row,col+1),(row,col-1)]
  newEmptyPos = grid[len(grid)-1][len(grid)-1].newX,grid[len(grid)-1][len(grid)-1].newY #new position of empty piece
  for i in neighbours:
    j,k = i
    if j < 0 or k < 0:
      continue
    try:
      if grid[j][k].x == newEmptyPos[0] and grid[j][k].y == newEmptyPos[1]:
        for i in range(len(grid)):
          for j in range(len(grid)):
            if grid[i][j].newX == grid[row][col].x and grid[i][j].newY == grid[row][col].y:
              a = grid[i][j]
            if grid[i][j].newX == newEmptyPos[0] and grid[i][j].newY == newEmptyPos[1]:
              b = grid[i][j]
              tempx,tempy = b.newX,b.newY
              b.newX,b.newY = grid[row][col].x,grid[row][col].y
              a.newX,a.newY = tempx,tempy
    except:
        pass





def init_grid():
  grid = [[None for i in range(4)] for i in range(4)]
  count = 1
  for i in range(ROWS):
      for j in range(COLS):
          grid[i][j] = piece(j*PIXEL_SIZE,i*PIXEL_SIZE,count,j*PIXEL_SIZE,i*PIXEL_SIZE)
          count += 1
  return grid
    

def draw_grid(screen,grid):
  count = 1
  for i in range(len(grid)):
    for j in range(len(grid)):
      currentPiece = grid[i][j]
      currentPiece.show(screen, currentPiece.newX , currentPiece.newY,currentPiece.number )
  
  if DRAW_GRID_LINES:
    for i in range(ROWS + 1):
      pygame.draw.line(screen, BLACK, (0,(i * PIXEL_SIZE)),(WIDTH, (i * PIXEL_SIZE)))
    for i in range(COLS + 1):
      pygame.draw.line(screen, BLACK, (i * PIXEL_SIZE, 0),(i * PIXEL_SIZE, HEIGHT))




def draw(screen):
  if started:
    screen.fill(BG_COLOUR)
    draw_grid(screen,shuffledGrid)
    draw_img(shuffledGrid)
  else:
    welcomeScreen()

started = False
running = True
initialGrid = init_grid()
shuffledGrid = shuffle(initialGrid)
save_img(shuffledGrid)

while running:
  clock.tick(FPS)
  keys = pygame.key.get_pressed()
  pos = pygame.mouse.get_pos()
  for event in pygame.event.get():
    if keys[K_SPACE]: started = True
    if started:
      if pygame.mouse.get_pressed()[0]:
          moveToEmpty(pos, shuffledGrid)
      
      if keys[K_SPACE]:
        shuffle(shuffledGrid)

      if won(shuffledGrid):
        print('you win!')

    
    
    if event.type == QUIT:
      running = False
    
    
  draw(screen)
  pygame.display.update()

pygame.quit()