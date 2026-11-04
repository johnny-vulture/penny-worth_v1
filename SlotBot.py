import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
)
from telegram.constants import ParseMode

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Stages
QUESTION1, QUESTION2, QUESTION3, QUESTION4, QUESTION5, RESULT = range(6)
# Callback data
ANSWER_A, ANSWER_B, ANSWER_C, ANSWER_D, RESTART, END = range(6)

questions = {
    QUESTION1: "Question 1: In Blackjack, what is the value of an Ace?\n"
               "A) 1\nB) 11\nC) 10\nD) 1 or 11",
    QUESTION2: "Question 2: What is the highest hand possible in standard Poker?\n"
               "A) Full House\nB) Straight Flush\nC) Royal Flush\nD) Four of a Kind",
    QUESTION3: "Question 3: In Roulette, what color is the number 0?\n"
               "A) Green\nB) Red\nC) Black\nD) Blue",
    QUESTION4: "Question 4: In a standard deck of cards, how many suits are there?\n"
               "A) 2\nB) 3\nC) 4\nD) 5",
    QUESTION5: "Question 5: What is the term for a hand of two cards of the same value in Poker?\n"
               "A) Flush\nB) Straight\nC) Full House\nD) Pair",
}

correct_answers = {
    QUESTION1: ANSWER_D,
    QUESTION2: ANSWER_C,
    QUESTION3: ANSWER_A,
    QUESTION4: ANSWER_C,
    QUESTION5: ANSWER_D,
}

user_answers = {}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Send message on `/start`."""
    global user_answers
    user_answers = {}  # Reset user answers at the start of the quiz

    user = update.message.from_user
    logger.info("User %s started the quiz.", user.first_name)

    # Welcome message
    welcome_message = ("<b>Welcome to the Trivia Quiz Bot! 🔎</b>\n\n"
                       "💰 Answer all 5 questions and claim your bonus! 💰\n"
                       "Press 'Start' to begin\n")

    # Initial question and answer options
    question_text = questions[QUESTION1]
    keyboard = [
        [
            InlineKeyboardButton("A", callback_data=str(ANSWER_A)),
            InlineKeyboardButton("B", callback_data=str(ANSWER_B)),
            InlineKeyboardButton("C", callback_data=str(ANSWER_C)),
            InlineKeyboardButton("D", callback_data=str(ANSWER_D)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_html(welcome_message)
    await update.message.reply_html(question_text, reply_markup=reply_markup)

    return QUESTION1


async def question_one(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    user_answers[QUESTION1] = (query.data == str(correct_answers[QUESTION1]))

    question_text = questions[QUESTION2]
    keyboard = [
        [
            InlineKeyboardButton("A", callback_data=str(ANSWER_A)),
            InlineKeyboardButton("B", callback_data=str(ANSWER_B)),
            InlineKeyboardButton("C", callback_data=str(ANSWER_C)),
            InlineKeyboardButton("D", callback_data=str(ANSWER_D)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(question_text, reply_markup=reply_markup)

    return QUESTION2


async def question_two(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    user_answers[QUESTION2] = (query.data == str(correct_answers[QUESTION2]))

    question_text = questions[QUESTION3]
    keyboard = [
        [
            InlineKeyboardButton("A", callback_data=str(ANSWER_A)),
            InlineKeyboardButton("B", callback_data=str(ANSWER_B)),
            InlineKeyboardButton("C", callback_data=str(ANSWER_C)),
            InlineKeyboardButton("D", callback_data=str(ANSWER_D)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(question_text, reply_markup=reply_markup)

    return QUESTION3


async def question_three(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    user_answers[QUESTION3] = (query.data == str(correct_answers[QUESTION3]))

    question_text = questions[QUESTION4]
    keyboard = [
        [
            InlineKeyboardButton("A", callback_data=str(ANSWER_A)),
            InlineKeyboardButton("B", callback_data=str(ANSWER_B)),
            InlineKeyboardButton("C", callback_data=str(ANSWER_C)),
            InlineKeyboardButton("D", callback_data=str(ANSWER_D)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(question_text, reply_markup=reply_markup)

    return QUESTION4


async def question_four(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    user_answers[QUESTION4] = (query.data == str(correct_answers[QUESTION4]))

    question_text = questions[QUESTION5]
    keyboard = [
        [
            InlineKeyboardButton("A", callback_data=str(ANSWER_A)),
            InlineKeyboardButton("B", callback_data=str(ANSWER_B)),
            InlineKeyboardButton("C", callback_data=str(ANSWER_C)),
            InlineKeyboardButton("D", callback_data=str(ANSWER_D)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(question_text, reply_markup=reply_markup)

    return QUESTION5


async def question_five(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    user_answers[QUESTION5] = (query.data == str(correct_answers[QUESTION5]))

    correct_count = sum(user_answers.values())

    if correct_count == 5:
        result_text = (
            f"Congratulations!! You answered all the questions correctly, Enjoy your bonus! Use Code : BIGQUIZ\n\n"
            
        )
    else:
        result_text = (
            f"You've completed the quiz!\n"
            f"You only got {correct_count}/5 correct answers, would you like to try again?\n"
        )

    keyboard = [
        [
            InlineKeyboardButton("Yes, let's do it again!",
                                 callback_data=str(RESTART)),
            InlineKeyboardButton("Nah, I've had enough ...",
                                 callback_data=str(END)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(result_text, reply_markup=reply_markup)

    return RESULT


async def restart(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Restart the quiz."""
    query = update.callback_query
    await query.answer()

    return await start(query, context)


async def end(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """End the quiz."""
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text="See you next time!")
    return ConversationHandler.END


def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(
        "").build()

    # Setup conversation handler with the states
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            QUESTION1: [
                CallbackQueryHandler(
                    question_one, pattern="^" + str(ANSWER_A) + "$"),
                CallbackQueryHandler(
                    question_one, pattern="^" + str(ANSWER_B) + "$"),
                CallbackQueryHandler(
                    question_one, pattern="^" + str(ANSWER_C) + "$"),
                CallbackQueryHandler(
                    question_one, pattern="^" + str(ANSWER_D) + "$"),
            ],
            QUESTION2: [
                CallbackQueryHandler(
                    question_two, pattern="^" + str(ANSWER_A) + "$"),
                CallbackQueryHandler(
                    question_two, pattern="^" + str(ANSWER_B) + "$"),
                CallbackQueryHandler(
                    question_two, pattern="^" + str(ANSWER_C) + "$"),
                CallbackQueryHandler(
                    question_two, pattern="^" + str(ANSWER_D) + "$"),
            ],
            QUESTION3: [
                CallbackQueryHandler(
                    question_three, pattern="^" + str(ANSWER_A) + "$"),
                CallbackQueryHandler(
                    question_three, pattern="^" + str(ANSWER_B) + "$"),
                CallbackQueryHandler(
                    question_three, pattern="^" + str(ANSWER_C) + "$"),
                CallbackQueryHandler(
                    question_three, pattern="^" + str(ANSWER_D) + "$"),
            ],
            QUESTION4: [
                CallbackQueryHandler(
                    question_four, pattern="^" + str(ANSWER_A) + "$"),
                CallbackQueryHandler(
                    question_four, pattern="^" + str(ANSWER_B) + "$"),
                CallbackQueryHandler(
                    question_four, pattern="^" + str(ANSWER_C) + "$"),
                CallbackQueryHandler(
                    question_four, pattern="^" + str(ANSWER_D) + "$"),
            ],
            QUESTION5: [
                CallbackQueryHandler(
                    question_five, pattern="^" + str(ANSWER_A) + "$"),
                CallbackQueryHandler(
                    question_five, pattern="^" + str(ANSWER_B) + "$"),
                CallbackQueryHandler(
                    question_five, pattern="^" + str(ANSWER_C) + "$"),
                CallbackQueryHandler(
                    question_five, pattern="^" + str(ANSWER_D) + "$"),
            ],
            RESULT: [
                CallbackQueryHandler(
                    restart, pattern="^" + str(RESTART) + "$"),
                CallbackQueryHandler(end, pattern="^" + str(END) + "$"),
            ],
        },
        fallbacks=[CommandHandler("start", start)],
    )

    # Add ConversationHandler to application that will be used for handling updates
    application.add_handler(conv_handler)

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
