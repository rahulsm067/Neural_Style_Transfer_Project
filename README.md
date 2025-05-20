![c6](https://github.com/user-attachments/assets/d1c87861-4774-4133-8aa5-304c48690bc5)
![c1](https://github.com/user-attachments/assets/2bc5529a-a290-42e6-b547-a9ec914b38ec)
![c6_s6](https://github.com/user-attachments/assets/7c888284-5cbb-4167-8e4d-4bfbd4a3630f)
![c1_s1](https://github.com/user-attachments/assets/9db03e01-b018-4c9e-8123-818ffd2a7d57)
![s6](https://github.com/user-attachments/assets/36ab72d9-7a0e-4696-b3d8-b7d6da01d92d)
![s1](https://github.com/user-attachments/assets/11d8296a-858f-4832-8634-e1971a66f8f7)
# Neural Style Transfer 🎨

This project implements Neural Style Transfer using TensorFlow and Streamlit. It blends the **content of one image** with the **style of another**, generating beautiful stylized images. The model uses a pre-trained TensorFlow `saved_model.pb` for style transfer.

---

## Project Structure
├── data/
│ ├── content-images/
│ ├── style-images/
│ └── output-images/
├── model/
│ ├── variables/
│ └── saved_model.pb # Pretrained style transfer model
├── notebooks/
│ └── neural_style_transfer.ipynb
├── venv/ # Python virtual environment
├── app.py # Streamlit Web Interface
├── Main.py # Model loading / image processing
├── README.md 
├── req.txt # Python dependencies

###  Step 1: Setup Environment

```bash
# Clone the repo
git clone https://github.com/rahulsm067/Neural-Style-Transfer-pro.git
cd NEURAL-STYLE-TRANSFER

# Create and activate virtual env
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r req.txt

# Run app.py

# if you want to train from scratch go in neural_style_transfer.ipynb and run one by one each cell



## 🖼️ Example

| Original Image | Style Image | Stylized Output |
|----------------|-------------|-----------------|
| ![content](./data/content-images/c1.jpg) | ![style](./data/style-images/s1.jpg) | ![output](./data/output-images/combined_c1_s1/c1_s1.jpg) |

![content](./data/content-images/c6.jpg) | ![style](./data/style-images/s6.jpg) | ![output](./data/output-images/combined_c6_s6/c6_s6.jpg) |

