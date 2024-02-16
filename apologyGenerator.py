from random import choice
# Apologies for Everyday Situations
# Apologies for Everyday Situations
everyday_apologies = [
    "I'm sorry for being late to the meeting; I lost track of time.",
    "Please forgive my forgetfulness; I'll set a reminder next time.",
    "I apologize for any inconvenience I may have caused.",
    "I'm sorry if my words or actions were hurtful.",
    "I didn't mean to upset you; I misunderstood the situation.",
    "I apologize for my thoughtlessness; I should have been more considerate.",
    "I'm sorry for forgetting to reply to your message earlier.",
    "Please accept my apologies for missing our appointment.",
    "I apologize for not returning your call; I've been swamped with work.",
    "I'm sorry for the confusion; I should have communicated more clearly.",
    "I'm sorry for not being there when you needed me.",
    "Please forgive me for the oversight; it won't happen again.",
    "I apologize for the delay in responding to your email.",
    "I'm sorry for the inconvenience; I'll do my best to make it right.",
    "Please accept my apologies for the inconvenience caused by the construction noise.",
    "I apologize for my absence at the event; unforeseen circumstances arose.",
    "I'm sorry for the misunderstanding; let's clarify things.",
    "Please forgive my mistake; I take full responsibility.",
    "I apologize for the confusion; I'll provide clarification.",
    "I'm sorry for the mix-up; it was an honest mistake."
]

# Apologies for Formal Situations (Corporate)
corporate_apologies = [
    "Please accept my sincerest apologies for the oversight.",
    "I apologize for the error; we will take immediate action to rectify it.",
    "I regret any inconvenience our mistake may have caused.",
    "I offer my deepest apologies for the misunderstanding.",
    "I apologize for any offense our statement may have given.",
    "I'm deeply sorry for the inconvenience; we strive for better service.",
    "I offer my sincerest apologies for falling short of your expectations.",
    "Please accept my apology; we value our partnership.",
    "I apologize for the delay in delivering the project; we encountered unexpected challenges.",
    "Please forgive our oversight; we will ensure it doesn't happen again.",
    "I apologize for any confusion caused by the recent policy change.",
    "I'm sorry for the inconvenience caused by the website maintenance.",
    "I apologize for any frustration caused by the technical issue; our team is working to resolve it.",
    "Please accept our apologies for the shipping delay; we are experiencing high demand.",
    "I'm sorry for the billing error; we will issue a refund promptly.",
    "I apologize for the inconvenience caused by the product recall.",
    "Please accept our sincerest apologies for the service disruption.",
    "I'm sorry for any inconvenience caused by the system upgrade.",
    "I apologize for the oversight in the contract; we will address it immediately.",
    "I'm sorry for the misunderstanding in the communication; we will provide clarification."
]

# Apologies for Humorous or Light-hearted Situations
humorous_apologies = [
    "I'm sorry for interrupting your daydream with my reality.",
    "I apologize for my pet rock's existential crisis; it's been a rocky road.",
    "Please forgive my inability to find your missing sock; it's gone on a solo adventure.",
    "I'm sorry I used up all the hot water; the faucet had separation anxiety.",
    "I apologize for not being a mind reader; my psychic powers are on vacation.",
    "Please accept my sincerest apologies for hogging the remote control; I got lost in the channels.",
    "I'm sorry for not speaking whale; my fish-to-English dictionary was missing.",
    "I apologize for mistaking you for a penguin; it was the tuxedo.",
    "Please forgive me for forgetting to water the plants; they're learning independence.",
    "I'm sorry for laughing at my own jokes; they're just too hilarious.",
    "I apologize for the popcorn mess; the movie was too intense.",
    "Please forgive the chaos; I tried to cook.",
    "I'm sorry for the confusion; I'm still trying to adult.",
    "I apologize for the confusion; my cat rearranged my files.",
    "Please forgive the mess; my inner child got carried away.",
    "I'm sorry for the noise; I was dancing in the shower.",
    "I apologize for the chaos; I'm renovating my life.",
    "Please forgive the disruption; I was chasing a dream.",
    "I'm sorry for the disruption; my imagination ran wild.",
    "I apologize for the confusion; I'm navigating through life's labyrinth."
]


def generate_apology(apology_type="everyday"):
    if apology_type == "everyday":
        return choice(everyday_apologies)
    elif apology_type == "corporate":
        return choice(corporate_apologies)
    elif apology_type == "humorous":
        return choice(humorous_apologies)
    else:
        raise ValueError("Invalid apology type")


if __name__ == "__main__":
    apology_type = input(
        "Enter the type (everyday, corporate, humour): ").lower()
    print(generate_apology(apology_type))
