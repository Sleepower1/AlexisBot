import discord
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont
import os
from keep_alive import keep_alive
import random


async def generate_meme(message_content, channel):
  # Open an image (replace 'paul.jpg' with the path to your meme template)
  new_dict = {"Upload Own Image Here"}
  num = random.randrange(0,len(new_dict))
  meme_template = Image.open(new_dict[num])

  # Get the dimensions of the image
  image_width, image_height = meme_template.size

  # Create a drawing object
  draw = ImageDraw.Draw(meme_template)

  # Set the fraction of image height as the starting font size
  img_fraction = 0.2
  fontsize = int(image_height * img_fraction)

  # Set the margin of the image as a fraction of image width and height
  margin = 0.05
  margin_width = int(image_width * margin)
  margin_height = int(image_height * margin)

  # Use a loop to find the appropriate font size by decreasing it gradually
  font = ImageFont.truetype('impact.ttf', size=fontsize)
  while True:
      # Split the message into two parts
      message = message_content.split()
      half_length = len(message) // 2
      top_text = " ".join(message[:half_length])
      bottom_text = " ".join(message[half_length:])

      # Calculate the width and height of each text part
      top_text_width, top_text_height = draw.textbbox((0, 0), top_text, font=font)[2:4]
      bottom_text_width, bottom_text_height = draw.textbbox((0, 0), bottom_text, font=font)[2:4]

      # Check if the text fits within the image with the margin
      if (top_text_width <= image_width - 2 * margin_width and
          top_text_height <= image_height / 2 - margin_height and
          bottom_text_width <= image_width - 2 * margin_width and
          bottom_text_height <= image_height / 2 - margin_height):
          # Text fits within the image
          break
      else:
          # Text does not fit, reduce the font size
          fontsize -= 1
          font = ImageFont.truetype('impact.ttf', size=fontsize)

  # Calculate the position to center the top text horizontally
  top_x = (image_width - top_text_width) / 2
  # Adjust the vertical position according to the top margin
  top_y = margin_height

  # Calculate the position to center the bottom text horizontally
  bottom_x = (image_width - bottom_text_width) / 2
  # Adjust the vertical position according to the bottom margin
  bottom_y = image_height - bottom_text_height - margin_height

  # Overlay the top text on the image with a black border
  draw.text((top_x, top_y), top_text, fill='white', font=font, stroke_width=5, stroke_fill='black')

  # Overlay the bottom text on the image with a black border
  draw.text((bottom_x, bottom_y), bottom_text, fill='white', font=font, stroke_width=5, stroke_fill='black')

  # Save the generated meme
  meme_template.save('new_meme.jpg')

  # Send the meme to the Discord channel
  await channel.send(file=discord.File('new_meme.jpg'))

  # Delete the paul1.jpg file
  os.remove('new_meme.jpg')
