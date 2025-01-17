from sklearn.datasets import _samples_generator
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.pipeline import Pipeline
from sklearn.ensemble import ExtraTreesClassifier

# Генерування даних
X, Y = _samples_generator.make_classification(n_samples=150, n_features=25, n_classes=3,
                                              n_informative=6,
                                              n_redundant=0, random_state=7)  # Вибір k найважливіших ознак
k_best_selector = SelectKBest(f_regression, k=10)
# Ініціалізація класифікатора на основі гранично випадкового лісу classifier = ExtraTreesClassifier(n_estimators=60, max_depth=4) # Створення конвеєра
processor_pipeline = Pipeline([('selector', k_best_selector), ('erf', classifier)])
# Встановлення параметрів
processor_pipeline.set_params(selectork = 7, erfn_estimators = 30)  # Навчання конвеєра
processor_pipeline.fit(X, Y)
# Прогнозування результатів для вхідних даних print("Predicted output:", processor_pipeline.predict(X)) # Виведення оцінки
print("Score:", processor_pipeline.score(X, Y))  # Виведення ознак, відібраних селектором конвеєра
status = processor_pipeline.named_steps['selector'].get_support()  # Вилучення та виведення індексів обраних ознак
selected = [i for i, x in enumerate(status) if x]
print("Selected features:", selected)
