# import labelbox
# import base64
# import io
# from PIL import Image
#
# LB_API_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJjbGhyamVoc2kwMTF0MDd6ODduZ282dGhiIiwib3JnYW5pemF0aW9uSWQiOiJjbGhyamVocjkwMTFzMDd6OGN3Y3Q5ODQ4IiwiYXBpS2V5SWQiOiJjbGk2NHU1NjUwMHdzMDd4eTFsaTAwZzkzIiwic2VjcmV0IjoiZjU1NDQ5MjlhODJmOTJhZGY3NzQyZTY3NGIyN2Y5ZGQiLCJpYXQiOjE2ODUyMDA0NDksImV4cCI6MjMxNjM1MjQ0OX0.WIeAMGbZr3p0GojMzPffUPCvjJLIUsk9W4riXCa8MvY'
# PROJECT_ID = 'clhro8btj006907zq1g8j0muu'  # Replace with your project ID
# EXPORT_FORMAT = 'mask_bmp'  # Specify the desired export format
#
# client = labelbox.Client(api_key=LB_API_KEY)
# project = client.get_project(PROJECT_ID)
#
# # Define export parameters including the format
# export_params = {
#     "format": EXPORT_FORMAT
# }
#
# # Initiate the export
# export_job = project.export_data_rows(params=export_params)
#
# # Wait for the export to complete
# export_job.wait_until_done()
#
# # Get the exported data
# export_data = export_job.get_output()
#
# # Process the exported data
# for data_row in export_data:
#     # Get the image mask data
#     mask_data = data_row['annotations'][0]['mask']['data']
#     mask_bytes = base64.b64decode(mask_data)
#
#     # Load the mask image using PIL
#     mask_image = Image.open(io.BytesIO(mask_bytes))
#
#     # Save the mask image
#     mask_image.save(f"./segmentedImages/label_{data_row['uuid']}.bmp")





# import labelbox
# LB_API_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJjbGhyamVoc2kwMTF0MDd6ODduZ282dGhiIiwib3JnYW5pemF0aW9uSWQiOiJjbGhyamVocjkwMTFzMDd6OGN3Y3Q5ODQ4IiwiYXBpS2V5SWQiOiJjbGk2NHU1NjUwMHdzMDd4eTFsaTAwZzkzIiwic2VjcmV0IjoiZjU1NDQ5MjlhODJmOTJhZGY3NzQyZTY3NGIyN2Y5ZGQiLCJpYXQiOjE2ODUyMDA0NDksImV4cCI6MjMxNjM1MjQ0OX0.WIeAMGbZr3p0GojMzPffUPCvjJLIUsk9W4riXCa8MvY'
# PROJECT_ID = 'clhro8btj006907zq1g8j0muu'
# client = labelbox.Client(api_key = LB_API_KEY)
# project = client.get_project(PROJECT_ID)
# labels = project.export_v2(params={
# 	"data_row_details": True,
# 	"metadata": True,
# 	"attachments": True,
# 	"project_details": True,
# 	"performance_details": True,
# 	"label_details": True,
# 	"interpolated_frames": True
#   })





import labelbox
import base64
import io
from PIL import Image

LB_API_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJjbGhyamVoc2kwMTF0MDd6ODduZ282dGhiIiwib3JnYW5pemF0aW9uSWQiOiJjbGhyamVocjkwMTFzMDd6OGN3Y3Q5ODQ4IiwiYXBpS2V5SWQiOiJjbGk2NHU1NjUwMHdzMDd4eTFsaTAwZzkzIiwic2VjcmV0IjoiZjU1NDQ5MjlhODJmOTJhZGY3NzQyZTY3NGIyN2Y5ZGQiLCJpYXQiOjE2ODUyMDA0NDksImV4cCI6MjMxNjM1MjQ0OX0.WIeAMGbZr3p0GojMzPffUPCvjJLIUsk9W4riXCa8MvY'
PROJECT_ID = 'clhro8btj006907zq1g8j0muu'  # Replace with your project ID
EXPORT_FORMAT = 'mask_bmp'  # Specify the desired export format

client = labelbox.Client(api_key=LB_API_KEY)
project = client.get_project(PROJECT_ID)

# Get the data rows for the project
data_rows = client.get_project_data_rows(project.uid)

# Define export parameters including the format
export_params = {
    "format": EXPORT_FORMAT,
    "data_row_ids": [data_row.uid for data_row in data_rows]
}

# Initiate the export
export_job = client.create_export_job(project.uid, export_params)

# Wait for the export to complete
export_job.wait_until_done()

# Get the exported data
export_data = export_job.get_output()

# Process the exported data
for data_row in export_data:
    # Get the image mask data
    mask_data = data_row['annotations'][0]['mask']['data']
    mask_bytes = base64.b64decode(mask_data)

    # Load the mask image using PIL
    mask_image = Image.open(io.BytesIO(mask_bytes))

    # Save the mask image
    mask_image.save(f"./segmentedImages/label_{data_row['uuid']}.bmp")

