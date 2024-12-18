from datetime import datetime
import random 
import requests 

c=datetime.now()
current_time=c.strftime('%H:%M')
year=c.year
month=c.month
day=c.day

major_cards = {
    "The Fool": "A rosebud, delicate and fragile has formed overnight. A new beginning is coming your way. It may be time to take a leap of faith.",
    "The Magician":"You have the skills you need for the task at hand.",
    "The High Priestess": "Drown out the other voices. Your path is known only to you.",
    "The Empress": "I bring you wealth: of ideas, of love, of abundance.",
    "The Emperor": "It might be time to return to the box. Structure is imperative to the foundation of a strong house.",
    "The Hierophant":"Now is the time to embrace tradition.",
    "The Lovers":"Two paths diverge. A choice must be made.",
    "The Chariot":"You are barrelling towards something. Do not stop.",
    "Strength":"Draw on all your reserves. Stay put. You are on the right path, even if it seems interminable.",
    "The Hermit":"Take some time for yourself.",
    "The Wheel":"A new cycle begins. Remember, the wheel always spins back.",
    "Justice":"Justice will be wrought, though the heavens may fall.",
    "The Hanged Man":"Step away from the situation.",
    "Death":"A full-stop is always followed by a new sentence.",
    "Temperance":"Yin and yang. There is a need for balance in times of excess.",
    "The Devil":"You are hostage to desires that do not serve you anymore.",
    "The Tower":"A storm of change is coming. Surrender.",
    "The Star":"You have endured the storm and survived. The possibilities are endless where hope holds fast.",
    "The Moon": "Some things may be obscured, but your subconscious will lead you. Pay particular attentions to your dreams at this time.",
    "The Sun": "You are blessed with success. Take a breath and enjoy.",
    "Judgement": "An important choice awaits you. Consider the outcomes with both head and heart.",
    "The World": "You have come full circle and have accomplished much."
}
def username():
        name=input("Welcome to Tarot Journal. What's your name? ")
        print("Welcome,",name)

def current():
        print("It is", current_time,"on",day,month,year)

def card_draw(major_cards):
        draw = int(input("How many cards do you want?"))
        return draw
        
        
def whichcards(draw):
        card_list = list(major_cards.items())
        selected_cards = random.sample(card_list, draw)

        for card in selected_cards:
                print(card)


username()
current()
draw=card_draw(major_cards)
whichcards(draw)
