import re
from alive_progress import alive_bar
from copy import deepcopy
from time import time
start = time()

class Tile:
    def __init__(self, id_, grid):
        self.idn = int(id_)
        self.pix = grid
        self.get_edges()
        self.extract_image()
        self.edge_matches = [None]*4

    def rotate_cw(self):
        rot_pix = ['']*len(self.pix[0])
        for rw in self.pix:
            for i in range(len(rw)):
                rot_pix[i] += rw[i]
        rot_pix = [rw[::-1] for rw in rot_pix]
        self.pix = rot_pix
        self.extract_image()

        self.get_edges()
        A, B, C, D = self.edge_matches
        self.edge_matches = [C, D, B, A]

    def reflect_x(self):
        self.pix = self.pix[::-1]
        self.extract_image()

        self.get_edges()
        A, B, C, D = self.edge_matches
        self.edge_matches = [B, A, C, D]

    def reflect_y(self):
        self.pix = [rw[::-1] for rw in self.pix]
        self.extract_image()

        self.get_edges()
        A, B, C, D = self.edge_matches
        self.edge_matches = [A, B, D, C]

    def extract_image(self):
        self.img = [rw[1:len(rw)-1] for rw in self.pix][1:len(self.pix)-1]
    
    def get_edges(self):
        # TOP, BOTTOM, LEFT, RIGHT
        self.edges = self.pix[:len(self.pix):len(self.pix)-1] + ['', '']
        for rw in self.pix:
            self.edges[2] += rw[0]
            self.edges[3] += rw[len(rw)-1]
        
        self.edge_codes = [self.encode_edge(E) for E in self.edges]

    def encode_edge(self, edge):
        edge = edge.replace('.', '0')
        edge = edge.replace('#', '1')
        codes = sorted([int(edge, 2), int(edge[::-1], 2)])
        return codes

    def id_edge_matches(self, other):
        for edge_ind in range(len(self.edge_codes)):
            if self.edge_codes[edge_ind] in other.edge_codes:
                self.edge_matches[edge_ind] = other.idn
    
    def is_corner(self):
        if self.edge_matches.count(None)==2:
            return True
        return False

    def show(self, raw=False):
        print("\nTile {}:".format(self.idn))
        if raw:
            for rw in self.pix:
                print(rw)
        else:
            for rw in self.img:
                print(rw)
    
    def __eq__(self, other):
        if self.idn==other.idn:
            return True
        return False

with open("2020/inputs/day_20_input.txt") as f:
    raw_data = f.readlines()

tiles = dict()
for ind in range(0, len(raw_data), 12):
    id_num = int(raw_data[ind][5:9])
    img = []
    for subind in range(1, 11):
        img.append(raw_data[ind+subind][:-1])
    tiles[id_num] = Tile(id_num, img)

#### PART 1 ####

print("\nLining up edges...")
with alive_bar(len(tiles)**2) as bar:
    for t1 in tiles.values():
        for t2 in tiles.values():
            bar()
            if not(t1.idn==t2.idn):
                t1.id_edge_matches(t2)

cnr_prod = 1
cnr_ids = []

print("\nIdentifying corners...")
with alive_bar(len(tiles)) as bar:
    for t1 in tiles.values():
        bar()
        if t1.is_corner():
            cnr_prod *= t1.idn
            cnr_ids.append(t1.idn)

print("\nThe product of the corner tile IDs is {}".format(cnr_prod))
print("Runtime: {} seconds".format(time()-start))

#### PART 2 ####

start = time()

def show_stitched(big_img, raw=False):
    print("\n")
    for rw in big_img:
        print(rw)
            
def fit_piece(placed, to_place, top, left):
    if top and left or not(top or left):
        print("Pick ONE of top and left")
        return
    
    if top:
        connecting_ind = 0
    if left: 
        connecting_ind = 2
    match_num = placed.idn
    while not(to_place.edge_matches[connecting_ind]==match_num):
        to_place.rotate_cw()
    while not(to_place.edges[connecting_ind]==placed.edges[connecting_ind+1]):
        if top:
            to_place.reflect_y()
        if left:
            to_place.reflect_x()

    return to_place

def stitch_image(pieces, nw_cnr):
    macro_img = []

    current_piece = pieces[nw_cnr]
    while current_piece.edge_matches[0] or current_piece.edge_matches[2]:
        current_piece.rotate_cw()
    macro_img.append([current_piece])
    bar()

    while current_piece.edge_matches[1] is not None:
        next_piece = pieces[current_piece.edge_matches[1]]
        macro_img.append([fit_piece(current_piece, next_piece, True, False)])
        bar()
        current_piece = next_piece

    for row_ind in range(len(macro_img)):
        current_piece = macro_img[row_ind][0]
        while current_piece.edge_matches[3] is not None:
            next_piece = pieces[current_piece.edge_matches[3]]
            macro_img[row_ind].append(fit_piece(current_piece, next_piece, False, True))
            bar()
            current_piece = macro_img[row_ind][-1]
    
    return_img = []
    for rw in macro_img:
        for j in range(len(rw[0].img)):
            return_row = ''
            for i in range(len(rw)):
                return_row += rw[i].img[j] # + " "
            return_img.append(return_row)

    return return_img

print("\nStitching together the image...")
with alive_bar(len(tiles)) as bar:
    full_img = stitch_image(tiles, cnr_ids[0])

monster = [ "                  # ", \
            "#    ##    ##    ###", \
            " #  #  #  #  #  #   " ]

monster_tests = [re.compile(S.replace(' ', '.')) for S in monster]

monster_size = (len(monster), len(monster[0]))
image_size = (len(full_img), len(full_img[0]))

def img_rot_cw(img):
    rot_pix = ['']*len(img[0])
    for rw in img:
        for i in range(len(rw)):
            rot_pix[i] += rw[i]
    rot_pix = [rw[::-1] for rw in rot_pix]
    return rot_pix

def img_refl_x(img):
    return img[::-1]

found = False
recourses = [img_rot_cw, img_rot_cw, img_rot_cw, img_refl_x, img_rot_cw, img_rot_cw, img_rot_cw]

while not(found):
    for rw in range(image_size[0] - monster_size[0]):
        for cl in range(image_size[1] - monster_size[1]):
            results = [re.match(monster_tests[i], full_img[rw+i][cl:]) for i in range(monster_size[0])]
            if all(results):
                found = True
    if not(found):
        if len(recourses)==0:
            found = True
            print("No monsters found in any configuration :(")
        else:
            transform = recourses.pop()
            full_img = transform(full_img)

print("\nLocating sea monsters...")
with alive_bar((image_size[0] - monster_size[0]) * (image_size[1] - monster_size[1])) as bar:
    annotated_map = deepcopy(full_img)
    for rw in range(image_size[0] - monster_size[0]):
        for cl in range(image_size[1] - monster_size[1]):
            bar()
            results = [re.match(monster_tests[i], full_img[rw+i][cl:]) \
                for i in range(monster_size[0])]
            if all(results):
                for i in range(monster_size[0]):
                    markup = ''
                    for j in range(monster_size[1]):
                        if monster[i][j]==' ':
                            markup += annotated_map[rw+i][cl+j]
                        if monster[i][j]=='#':
                            markup += '█'
                    annotated_map[rw+i] = annotated_map[rw+i][:cl] + markup \
                        + annotated_map[rw+i][cl+len(markup):]

show_stitched(annotated_map)

roughness = 0
for line in annotated_map:
    roughness += line.count('#')

print("\nThe habitat's water roughness is {}".format(roughness))
print("Runtime: {} seconds".format(time()-start))

#                   █
# █    ██    ██    ███
#  █  █  █  █  █  █