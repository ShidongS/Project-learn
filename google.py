
# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


def run_quickstart():
    # [START vision_quickstart]
    import io
    import os
    import PIL
    from PIL import ImageFont
    from PIL import Image
    from PIL import ImageDraw

    # Imports the Google Cloud client library
    # [START vision_python_migration_import]
    from google.cloud import vision
    from google.cloud.vision import types
    # [END vision_python_migration_import]

    # Instantiates a client
    # [START vision_python_migration_client]
    client = vision.ImageAnnotatorClient()
    # [END vision_python_migration_client]

    # The name of the image file to annotate
    i=0
    for root,dir,files in os.walk('/home/gary/EC601/picture/'):
        i+=len(files)
    print(i)
    for k in range(1,i+1):
        file_name = os.path.join(os.path.dirname(__file__),'/home/gary/EC601/picture/'+'%04d'%(k)+'.jpg')

    # Loads the image into memory
        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()

        image = types.Image(content=content)

    # Performs label detection on the image file
        response = client.label_detection(image=image)
        labels = response.label_annotations
        print('Labels:')
        for label in labels:
            print(label.description)
            tag=label.description
        im1=Image.open('/home/gary/EC601/picture/'+'%04d'%(k)+'.jpg')
        font = ImageFont.truetype("/usr/share/fonts/truetype/ttf-dejavu/DejaVuSans.ttf",40)
        draw = ImageDraw.Draw(im1)
        draw.text((0, 0),tag,(255,255,0),font=font)
        draw = ImageDraw.Draw(im1)
        im1.save('/home/gary/EC601/picture2/'+'%04d'%(k)+'.jpg')
    # [END vision_quickstart]


if __name__ == '__main__':
    run_quickstart()
