


a=['party_head','veil_bottom']
b=['veil_head','science_head']
c=['science_bottom','veil_bottom']
d=['veil_head','crimson_head']
dd=['crimson_bottom','science_head']
e=['science_bottom','spandex_head']
f=['spandex_bottom','science_bottom']
g=['science_head','space_head']
h=['space_bottom','spandex_bottom']
i=['spandex_head','art_bottom']
j=['art_head','party_head']
k=['party_bottom','crimson_bottom']
l=['crimson_head','art_bottom']
m=['art_head','space_head']
n=['space_bottom','party_head']
o=['party_bottom','science_bottom']
p=['science_head','art_bottom']
q=['art_head','crimson_head']
r=['crimson_bottom','spandex_head']
s=['spandex_bottom','party_bottom']
t=['party_head','art_bottom']
u=['art_head','veil_head']
v=['veil_bottom','space_bottom']
w=['space_head','crimson_head']
x=['crimson_bottom','space_head']
y=['space_bottom','veil_head']
z=['veil_bottom','spandex_bottom']
zz=['spandex_head','party_bottom']


cards = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,w,z,dd,zz]


player_1_cards_played=[]
player_2_cards_played=[]



print(len(cards))

def find_playable_cards_in_hand(hand,board):
    """ returns cards in hand that can be played on board"""

    possible_plays=[]
    accessible_chain_ends  = [0,-1]

    for end in accessible_chain_ends:
        for card in hand:
            for side in card:

                if side.split('_')[0] == board[end][end].split('_')[0]:     #check for same lama type

                    if side.split('_')[1] != board[end][end].split('_')[1]:    # check for opposite lama pose, it head > bottom or bottom > head

                        #determine playable rotation
                        if (side == card[0]) and (end == -1):
                            rotation = card
                        if (side == card[1]) and (end == -1):
                            rotation = card[::-1]
                        if (side == card[0]) and (end == 0):
                            rotation = card[::-1]
                        if (side == card[1]) and (end == 0):
                            rotation = card

                        print('\n')
                        print('card '+str(card)+' can be played at board end '+str(end)+' '+str(board[end])+' in rotation '+str(rotation))
                        print('\n')
                        possible_plays.append([card,rotation,end])    # need to store card and playable direction and place card needs to be played to be valid

    return possible_plays

# board=[a,b,c]
# hand=[d,zz]
#
# print(find_playable_cards_in_hand(hand,board))




def choose_card(playable_cards):
    """ chooses card to play from playable card list, should probably have access to all the variables an actual player would """

    playing = playable_cards[0]
    print('\n choosing \n', playing)

    return   playing # for now





def game(cards):

    print('\n starting deck \n \n ',cards)
    #shuffle deck
    import random
    random.shuffle(cards)
    print('\n shuffled deck \n \n ',cards)

    #generate starting board
    board=[]
    board.append(cards[0])   #drawing
    cards = cards[1:]


    #playing loop
    hand1 =cards[0:5]
    cards = cards[6:]
    hand2 = cards[0:5]
    cards=cards[6:]
    print('\n hands \n ',hand1,hand2,len(hand1),len(hand2))
    hands = [hand1,hand2]

    choices1=[]
    choices2=[]
    choices=[choices1,choices2]
    for i in range(100):
        print('\n turn \n ',i)
        for j in range(len(hands)):
            playable = find_playable_cards_in_hand(hands[j],board)
            choices[j].append(len(playable))
            if len(playable)<1:
                print('unable to play card, drawing')
                print(playable,len(playable))
                if len(cards)>0:
                    hand1.append(cards[0])
                    cards = cards[1:]
                if len(cards)==0:
                    print('unable to draw, deck is empty')
            if len(playable)>=1:
                print('PLAYABLE',playable,len(playable))

                playing = choose_card(playable)
                print('PLAYING', playing, playing[2],playing[2]==0,playing[2]==-1)
                if playing[2] == 0:
                    print('prepending')
                    board.insert(0,playing[1])
                    hands[j].remove(playing[0])
                if playing[2] == -1:
                    print('appending')
                    board.append(playing[1])
                    hands[j].remove(playing[0])

            print('\n new board \n ', board, len(board))
            print('\n player hands \n ',hand1,len(hand1),hand2,len(hand2))





    print(choices)
    return #winner,board




game(cards)
