async function calculateValue() {
    try {
        // 验证数字输入的有效性
        const validateNumberInput = (inputId, min, max) => {
            const inputElement = document.getElementById(inputId);
            const value = parseFloat(inputElement.value);
            
            if (isNaN(value)) {
                throw `Please enter a valid number for ${inputElement.previousElementSibling.textContent}`;
            }
            if (value < min || value > max) {
                throw `${inputElement.previousElementSibling.textContent} must be between ${min}-${max}`;
            }
            return value;
        };

        // 收集所有表单数据
        const formData = {
            overall: validateNumberInput('overall', 40, 99),
            potential: validateNumberInput('potential', 40, 99),
            age: validateNumberInput('age', 16, 54),
            club_position: document.getElementById('club_position').value,
            weak_foot: validateNumberInput('weak_foot', 1, 5),
            skill_moves: validateNumberInput('skill_moves', 1, 5),
            international_reputation: validateNumberInput('international_reputation', 1, 5),
            work_rate: document.getElementById('work_rate').value,
            body_type: document.getElementById('body_type').value
        };

        // 发送数据到后端API
        const response = await fetch('http://localhost:5000/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData)
        });

        // 处理响应
        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.error || 'Calculation failed');
        }

        // 格式化并显示结果
        const result = await response.json();
        const currencyFormatter = new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: 'EUR',
            minimumFractionDigits: 0,
            maximumFractionDigits: 0
        });

        document.getElementById('market-value').textContent = currencyFormatter.format(result.market_value);
        document.getElementById('weekly-salary').textContent = currencyFormatter.format(result.weekly_salary);

    } catch (error) {
        alert(`Error: ${error.message}`);
        // 重置结果显示
        document.getElementById('market-value').textContent = '-';
        document.getElementById('weekly-salary').textContent = '-';
    }
}