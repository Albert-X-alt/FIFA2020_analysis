from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import torch
import pandas as pd
from FIFA22 import FIFA_dataset
from model import simpleMLP

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return app.send_static_file('index.html')

# 初始化数据集获取标准化参数
df = pd.read_excel('player.xlsx')
dataset = FIFA_dataset(df)

# 加载模型
model = simpleMLP(9, 1)
model.load_state_dict(torch.load('best_model1.pth', map_location=torch.device('cpu')))
model.eval()
model.to('cpu')



@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json

        # 按特征顺序[5,6,9,17,28,29,30,31,32]处理输入
        features = [
            float(data['overall']),        # 特征5
            float(data['potential']),      # 特征6
            float(data['age']),            # 特征9 (age)
            dataset.feature_mappings[17].get(data['club_position'], 0),  # 特征17
            float(data['weak_foot']),      # 特征28
            float(data['skill_moves']),    # 特征29
            float(data['international_reputation']),  # 特征30 (international_reputation)
            dataset.feature_mappings[31].get(data['work_rate'], 0),  # 特征31
            dataset.feature_mappings[32].get(data['body_type'], 0)   # 特征32
        ]

        # 转换为Tensor
        input_tensor = torch.FloatTensor(features).unsqueeze(0).to('cpu')

        # 预测
        with torch.no_grad():
            prediction = model(input_tensor)
            denormalized = prediction.item() * dataset.target_std + dataset.target_mean

        return jsonify({
            'market_value': round(denormalized, 2),
            'weekly_salary': round(denormalized / 52, 2)
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)