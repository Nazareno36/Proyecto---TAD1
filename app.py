import pygame
from button import Button
from combo_box import ComboBox
from card import Card
from deck import Deck
from binary_tree import BinaryTree
from graph import Graph
from text_field import TextField
from pygame.locals import *
import random
import math
import json

class App:

    def __init__(self):
        #screen
        self.size = width, height = (800,600)
        self.running = True
        self.screen = pygame.display.set_mode(self.size) 
        pygame.display.set_caption("Reto 2")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None,30)

        #principal Buttons:
        self.stack_buttons = Button(140,550,60,30,'pilas')
        self.trees_button = Button(360,550,80,30,'arboles')
        self.graph_button = Button(600,550,70,30,'grafos')

        #Game variables:
        self.deck1 = Deck(50,50)
        self.init_deck1()
        self.deck2 = Deck(300,50)
        self.init_deck2()
        self.deck3 = Deck(550,50)
        self.init_deck3()
        self.selected_card = None
        self.game_win = False
        
        #tree Variables:
        self.tree = BinaryTree(10)
        self.combo_box = ComboBox(50,50,110,30,['pre order','in order','post order'])
        self.traversal_button = Button(170,50,100,30,'Traversal')
        self.value_field = TextField(560,60,50,30)
        self.insert_button = Button(620,60,80,30,'insertar')
        self.output_field = TextField(50,500,300,30)

        # self.tree.insert(5)
        # self.tree.insert(2)
        # self.tree.insert(1)
        # self.tree.insert(3)
        # self.tree.insert(4)
        # self.tree.insert(7)
        # self.tree.insert(6)
        # self.tree.insert(9)
        # self.tree.insert(8)

        #Graph variables:
        self.map = pygame.transform.scale(pygame.image.load('assets/Images/Map.jpeg'),(650,450))
        self.graph_data = self.load_json()
        self.cities_id = []
        self.cities_name = []
        for city in self.graph_data:
            self.cities_name.append(city['name'])
            self.cities_id.append(city['id'])    
        print(self.cities_name)
        self.graph = Graph()
        self.result_graph = Graph()
        self.init_graph(self.graph)
        self.init_graph(self.result_graph)    
        self.origin_combo = ComboBox(50,40,60,30,self.cities_id)
        self.destination_combo = ComboBox(110,40,60,30,self.cities_id)
        self.weight_field = TextField(177.5,40,50,30)
        self.set_button = Button(235,40,80,30,'Setear')
        self.search_button = Button(325,40,80,30,'Buscar')
        self.random_button = Button(555.5,40,85,30,'Random')
        self.show_button = Button(645,40,50,30,'ver')
        self.route_output = TextField(50,517.5,300,30)


    def reset_state(self):
        self.stack_buttons.actioned = False
        self.trees_button.actioned = False
        self.graph_button.actioned = False

    #Draw methods
    def draw_buttons(self):
        self.stack_buttons.draw(self.screen,(215,214,227))
        self.trees_button.draw(self.screen,(215,214,227))
        self.graph_button.draw(self.screen,(215,214,227))

    def draw_decks(self):
        self.deck1.draw(self.screen)
        self.deck2.draw(self.screen)
        self.deck3.draw(self.screen)

    def draw_trees_interface(self):
        self.combo_box.draw(self.screen,(215,214,227))
        self.traversal_button.draw(self.screen,(215,214,227))
        self.value_field.draw(self.screen)
        self.insert_button.draw(self.screen,(215,214,227))
        self.output_field.draw(self.screen)

    def draw_graph_interface(self):
        self.weight_field.draw(self.screen)
        self.set_button.draw(self.screen,(215,214,227))
        self.search_button.draw(self.screen,(215,214,227))
        self.random_button.draw(self.screen,(215,214,227))
        self.show_button.draw(self.screen,(215,213,227))
        self.route_output.draw(self.screen)
        self.origin_combo.draw(self.screen,(215,214,227))
        self.destination_combo.draw(self.screen,(215,214,227))

    def init_deck1(self):
        self.deck1.push(Card(2,'assets/Images/card_2t.png'))
        self.deck1.push(Card(3,'assets/Images/card_3t.png')) 
        self.deck1.push(Card(4,'assets/Images/card_4t.png')) 
        self.deck1.push(Card(5,'assets/Images/card_5t.png')) 
        self.deck1.push(Card(6,'assets/Images/card_6t.png')) 

    def init_deck2(self):
        self.deck2.push(Card(7,'assets/Images/card_7t.png'))
        self.deck2.push(Card(8,'assets/Images/card_8t.png'))
        self.deck2.push(Card(9,'assets/Images/card_9t.png'))
        self.deck2.push(Card(10,'assets/Images/card_10t.png'))

    def init_deck3(self):
        self.deck3.push(Card(14,'assets/Images/card_At.png'))
        self.deck3.push(Card(13,'assets/Images/card_Kt.png'))
        self.deck3.push(Card(12,'assets/Images/card_Qt.png'))
        self.deck3.push(Card(11,'assets/Images/card_Jt.png'))

    def init_graph(self,graph):
        graph.insert(self.cities_id[0],120,110)
        graph.insert(self.cities_id[1],270,289)
        graph.insert(self.cities_id[2],310,130)
        graph.insert(self.cities_id[3],390,230)
        graph.insert(self.cities_id[4],340,289)
        graph.insert(self.cities_id[5],230,310)
        graph.insert(self.cities_id[6],290,150)
        graph.insert(self.cities_id[7],420,210)
        graph.insert(self.cities_id[8],540,500)
        graph.insert(self.cities_id[9],270,250)
        graph.insert(self.cities_id[10],270,185)
        graph.insert(self.cities_id[11],280,340)
        graph.insert(self.cities_id[12],260,270)
        graph.insert(self.cities_id[13],190,380)
        graph.insert(self.cities_id[14],410,130)
        graph.insert(self.cities_id[15],190,160)
        graph.insert(self.cities_id[16],390,150)
        graph.insert(self.cities_id[17],370,300)

    def set_graph_edges(self):
        for city in self.graph_data:
            for destination in city['destinations']:
                self.graph.add_edge(city['id'],destination,random.randint(1,50),False)
    
    def set_result_graph_edges(self,results):
        self.result_graph.clear_edges()
        for i in range(len(results)-1):
            origin = self.graph.nodes[int(results[i])].value
            destination = self.graph.nodes[int(results[i+1])].value
            self.result_graph.add_edge(origin,destination,self.graph.adjacency[int(results[i])][int(results[i+1])],False)

    def load_json(self):
        with open('ciudades.json') as data:
            data = json.load(data)
            return data

    def draw_win_screen(self):
        text_surface = self.font.render('¡Has Ganado!',True,(174,0,34))
        self.screen.blit(text_surface,(400-(text_surface.get_width()/2),300-(text_surface.get_height()/2)))

    #Update methods
    def menu_update(self,event):
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            if  self.stack_buttons.rect.collidepoint(event.pos): 
                self.reset_state()
                self.stack_buttons.actioned = True
            elif self.trees_button.rect.collidepoint(event.pos):
                self.reset_state()
                self.trees_button.actioned = True
            elif self.graph_button.rect.collidepoint(event.pos):
                self.reset_state()
                self.graph_button.actioned = True

    def stacks_scene_update(self,event):
        if event.type == MOUSEBUTTONDOWN and event.button==1:
            
            if self.game_win and self.stack_buttons.rect.collidepoint(event.pos):
                self.deck1 = Deck(50,50)
                self.init_deck1()
                self.deck2 = Deck(300,50)
                self.init_deck2()
                self.deck3 = Deck(550,50)
                self.init_deck3()
                self.selected_card = None
                self.game_win = False
            else:
                if self.deck1.rect.collidepoint(event.pos):
                    if self.selected_card:
                        if(not self.deck1.stack.tail or self.deck1.stack.tail.value.value > self.selected_card.value):
                            self.deck1.push(self.selected_card)
                            self.selected_card = None
                    else:
                        self.selected_card = self.deck1.pop()
                if self.deck2.rect.collidepoint(event.pos):
                    if self.selected_card:
                        if(not self.deck2.stack.tail or self.deck2.stack.tail.value.value > self.selected_card.value):
                            self.deck2.push(self.selected_card)
                            self.selected_card = None
                    else:
                        self.selected_card = self.deck2.pop()
                if self.deck3.rect.collidepoint(event.pos):
                    if self.selected_card:
                        if(not self.deck3.stack.tail or self.deck3.stack.tail.value.value > self.selected_card.value):
                            self.deck3.push(self.selected_card)
                            self.selected_card = None
                    else:
                        self.selected_card = self.deck3.pop()
                        
        if self.selected_card: 
            self.selected_card.translate(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
        if not self.game_win: self.game_win = self.deck1.is_ordered() or self.deck2.is_ordered() or self.deck3.is_ordered()

    def tree_scene_update(self,event):
        if event.type == MOUSEBUTTONDOWN and event.button==1:

            self.combo_box.update(event.pos)
            self.value_field.active = self.value_field.rect.collidepoint(event.pos)
            if self.insert_button.rect.collidepoint(event.pos):
                self.tree.insert(int(self.value_field.text))
            if self.traversal_button.rect.collidepoint(event.pos):
                if self.combo_box.option == 0: self.output_field.text = str(self.tree.preorder_traversal())
                if self.combo_box.option == 1: self.output_field.text = str(self.tree.inorder_traversal())
                if self.combo_box.option == 2: self.output_field.text = str(self.tree.postorder_traversal())

        if event.type == KEYDOWN:

            if self.value_field.active:
                if event.key == K_BACKSPACE:
                    self.value_field.text = self.value_field.text[:-1]
                else:
                    self.value_field.text+= event.unicode

    def graph_scene_update(self,event):
        if event.type == MOUSEBUTTONDOWN and event.button==1:
            self.origin_combo.update(event.pos)
            self.destination_combo.update(event.pos)
            self.weight_field.active = self.weight_field.rect.collidepoint(event.pos)
            if self.random_button.rect.collidepoint(event.pos):
                self.search_button.actioned = False
                self.set_graph_edges()
                self.random_button.actioned = True
            if self.show_button.rect.collidepoint(event.pos):
                self.search_button.actioned = False

            if self.random_button.actioned and self.search_button.rect.collidepoint(event.pos):
                origin = self.origin_combo.options[self.origin_combo.option].text
                destination = self.destination_combo.options[self.destination_combo.option].text
                result = self.graph.dijkstra(self.graph.index(origin),self.graph.index(destination))
                self.route_output.text = ''
                for position in result[1]:
                    self.route_output.text+= self.graph.nodes[position].value + ', '
                self.route_output.text += '  Distance: ' + str(result[0])
                self.set_result_graph_edges(result[1])
                self.search_button.actioned = True
            
            if self.search_button.actioned == False and self.set_button.rect.collidepoint(event.pos):
                origin = self.origin_combo.options[self.origin_combo.option].text
                destination = self.destination_combo.options[self.destination_combo.option].text
                weight = int(self.weight_field.text)
                self.graph.set_edge_weight(origin,destination,weight,False)

                
            
        if event.type == KEYDOWN:

            if self.weight_field.active:
                if event.key == K_BACKSPACE:
                    self.weight_field.text = self.weight_field.text[:-1]
                else:
                    self.weight_field.text+= event.unicode


    def draw(self):
        if self.stack_buttons.actioned: 
            if not self.game_win:
                self.draw_decks()
                if self.selected_card: self.selected_card.draw(self.screen)
            else:
                self.draw_win_screen()
        elif self.trees_button.actioned:
            self.tree.draw(self.screen)
            self.draw_trees_interface()
        elif self.graph_button.actioned:
            self.screen.blit(self.map,(52.5,75))
            self.result_graph.draw(self.screen) if self.search_button.actioned else self.graph.draw(self.screen)
            self.draw_graph_interface()
        self.draw_buttons()
        pygame.display.flip()

    def update(self,event):
        self.menu_update(event)
        if self.stack_buttons.actioned: self.stacks_scene_update(event)
        if self.trees_button.actioned: self.tree_scene_update(event)
        if self.graph_button.actioned: self.graph_scene_update(event)

    def start(self):
        while self.running:
            self.screen.fill((31,39,60))
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                self.update(event)
            
            self.draw()
            self.clock.tick(60)

pygame.init()
app = App()
app.start()
pygame.quit()