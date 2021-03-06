# Một số file import global
- setting.py : Chứa cấu hình Width, height,...
- gpath.py : Global PATH chứa các path tới một số thư mục trong project


# Các thư mục cần để ý
## Đối tượng Game: pacman, coin, monster,.. 
- layers/entity : Chứa các đối tượng Pacman, Monster, Ground,...
```python
    def render_tile(self, surface, position=None, angle=None):
    
```
- Nhớ import Vector2
>> from pygame.math import Vector2\
```python
    m = Monster(None, Vector2())
    m.render_tile(surface)
    #với surface là window trong hàm render của screen hoặc bất cứ surface tạo ra khác
    
    # Nếu muốn set positon có hàm 
    m.set_position(x,y) 
    
    # Chi tiết các hàm được kế thừa từ Layer.py trong cùng thư mục entity
    # Mẫu render các đối tượng thực tế trong game ở màn hình PlayGameScreen và Class TileManager
```
## TileManager
- Đọc quản lý map, chi tiết xme ở cores/TileManager. Được sử dụng trong màn hình PlayGameScreen
- Trong TileManager này có hàm solve1_2 tham khảo thêm để viết lại level1 + 

# Thêm một màn hình mới
Bước 1: Thêm screen state ở state/EScreenState 

- Ví dụ: GameLevel1 = 5

```python
class EScreenState(enum.Enum):
    Playing = 1
    Option = 2
    Menu = 3
    Minimax = 4
```
Bước 2: Tạo màn hình trong screens

```python
from screens import GameScreen
import pygame
from gpath import *
from states import *


class MenuScreen(GameScreen):
    def __init__(self, state):
        GameScreen.__init__(self, state)
        print("- Create Screen")

    def on_key_down(self, event):
        pass
    def on_exit(self):
        print("Goodbye !")

    def process_input(self):
        for event in pygame.event.get():
            self.on_event(event)

    def update(self):
        pass

    def render(self, window):
        pass

    def clean(self):
        pass

```
> Nhớ vào __init__.py thêm dòng mới để python nhận class
> Template mẫu như trên, sửa các hàm on_key_down, update, render, clean. Process_input nhớ để 2 dòng như mẫu không game sẽ bị crash

Bước 2: Thêm luật cho screen state để game khởi tạo màn hình ở MasterState 
- Thêm vào switcher thuộc tính mới tương tự 3 màn hình 
```python
    
    def setActiveScreen(self, es_state: EScreenState):
        switcher = {
            EScreenState.Menu: MenuScreen(self),
            EScreenState.Playing: PlayGameScreen(self),
            EScreenState.Minimax: MinimaxGameScreen(self)
        }
        self.screen_state = es_state
        self.active_screen = switcher.get(es_state, None)

```


Bước 3: `pacman.py` có dòng sau để init giá trị mặc định hiện tại của màn hình. Thay đổi screen_state = màn hình của mình để test.
```python
        self.master_state = MasterState(
            window=self.window, running=True, screen_state=EScreenState.Minimax)
        self.clock = pygame.time.Clock()
```
> Xem cấu trúc trong screens/MenuScreen hay PlayGameScreen để làm tương tự



