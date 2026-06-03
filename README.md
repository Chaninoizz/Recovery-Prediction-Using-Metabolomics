# MetaboRecovery AI

## Metabolomics-Based Clinical Decision Support System for Recovery Outcome Prediction and Biomarker Discovery

# Executive Summary

MetaboRecovery AI เป็นระบบ Clinical Decision Support System (CDSS) ที่พัฒนาขึ้นเพื่อวิเคราะห์ข้อมูล Metabolomics ของผู้ป่วยหลังการผ่าตัด โดยใช้ Machine Learning และ Explainable AI เพื่อทำนายผลการฟื้นตัวของผู้ป่วย ค้นหา Biomarkers ที่มีความสำคัญ และสร้างรายงานเชิงคลินิกที่สามารถอธิบายเหตุผลของการทำนายได้อย่างโปร่งใส

จุดเด่นของโครงการคือการผสาน Biomarker Discovery, Explainable AI และ Clinical Interpretation เข้าไว้ในระบบเดียว ทำให้ผลลัพธ์ของ AI ไม่ได้เป็นเพียงการทำนายผลลัพธ์ แต่สามารถระบุ Biomarkers สำคัญ วิเคราะห์ความเสี่ยง และตีความรูปแบบทางเมตาบอลิซึมที่เกี่ยวข้องกับภาวะต่าง ๆ ได้

---

# Problem Statement

การฟื้นตัวหลังการผ่าตัดมีความแตกต่างกันในผู้ป่วยแต่ละราย โดยในปัจจุบันการประเมินความเสี่ยงส่วนใหญ่ยังอาศัยข้อมูลทางคลินิกและการติดตามอาการ ทำให้การคาดการณ์ผลการฟื้นตัวล่วงหน้ามีข้อจำกัด

ในขณะเดียวกัน เทคโนโลยี Metabolomics สามารถสะท้อนการเปลี่ยนแปลงทางชีวภาพของร่างกายในระดับโมเลกุล ทำให้สามารถค้นหา Biomarkers ที่เกี่ยวข้องกับผลลัพธ์ทางคลินิกได้

โครงการนี้จึงมุ่งพัฒนาระบบ AI ที่สามารถใช้ข้อมูล Metabolomics เพื่อสนับสนุนการประเมินแนวโน้มการฟื้นตัวของผู้ป่วย พร้อมทั้งค้นหา Biomarkers สำคัญและสร้างคำอธิบายเชิงคลินิกที่สามารถนำไปใช้ได้จริง

---

# Objectives

1. ทำนายผลการฟื้นตัวของผู้ป่วยหลังการผ่าตัด
2. ค้นหา Biomarkers ที่มีความสำคัญต่อผลการฟื้นตัว
3. อธิบายผลการตัดสินใจของ AI ด้วย Explainable AI
4. วิเคราะห์ Metabolic Patterns เพื่อช่วยสนับสนุนการตีความเชิงคลินิก
5. พัฒนา Dashboard และ Clinical Report Prototype สำหรับการใช้งานจริง

---

# Dataset

ข้อมูลที่ใช้พัฒนาระบบมาจากชุดข้อมูล Metabolomics ของผู้ป่วยหลังการผ่าตัด

Dataset Characteristics

- จำนวนผู้ป่วยทั้งหมด 47 ราย
- ข้อมูลจาก NMR Metabolomics
- ประกอบด้วยข้อมูล Biomarkers หลายชนิด
- Outcome Labels
  - Fast Recovery
  - Poor Recovery

Dataset ถูกนำมาผ่านกระบวนการเตรียมข้อมูลและคัดเลือก Biomarkers ที่มีความสำคัญต่อการทำนายผลการฟื้นตัว

---

# System Workflow

Metabolomics Data
↓
Data Cleaning
↓
Missing Value Handling
↓
Feature Engineering
↓
Data Standardization
↓
Feature Selection
↓
Champion Model Selection
↓
Recovery Outcome Prediction
↓
Biomarker Interpretation
↓
Metabolic Pattern Analysis
↓
Clinical AI Report
↓
Clinical Dashboard

---

iant="document" id="92614"}
# Data Processing Pipeline

เพื่อให้ได้โมเดลที่มีความแม่นยำสูงและสามารถอธิบายผลลัพธ์ทางคลินิกได้อย่างน่าเชื่อถือ ทีมงานได้ออกแบบ Data Processing Pipeline แบบหลายขั้นตอน โดยครอบคลุมตั้งแต่การเตรียมข้อมูลดิบไปจนถึงการคัดเลือก Biomarkers ที่เหมาะสมสำหรับการสร้าง Champion Model

---

## 1. Data Quality Assessment and Data Cleaning

ข้อมูล Metabolomics ดิบถูกนำมาตรวจสอบคุณภาพก่อนเข้าสู่กระบวนการสร้างโมเดล

ขั้นตอนประกอบด้วย

### Data Consistency Checking

ตรวจสอบความสอดคล้องของข้อมูลในแต่ละตัวแปร

- ตรวจสอบชื่อ Biomarkers
- ตรวจสอบชนิดข้อมูล (Data Types)
- ตรวจสอบความสมบูรณ์ของข้อมูลผู้ป่วย

### Outlier Screening

ตรวจสอบค่าที่ผิดปกติอย่างรุนแรงซึ่งอาจเกิดจาก

- เครื่องมือวัด
- การบันทึกข้อมูลผิดพลาด
- ความคลาดเคลื่อนจากกระบวนการทดลอง

### Duplicate Verification

ตรวจสอบข้อมูลซ้ำเพื่อป้องกันการเกิด Bias ในการฝึกโมเดล

ผลลัพธ์ของขั้นตอนนี้คือชุดข้อมูลที่มีความสอดคล้องและพร้อมสำหรับการวิเคราะห์เชิงสถิติ

---

## 2. Missing Value Handling

ข้อมูลทางการแพทย์มักมีค่าที่หายไป (Missing Values) ซึ่งอาจส่งผลต่อประสิทธิภาพของโมเดล

ทีมงานดำเนินการ

### Missing Data Analysis

- ตรวจสอบจำนวนค่าที่หายไปในแต่ละ Biomarker
- วิเคราะห์รูปแบบการหายไปของข้อมูล

### Missing Value Treatment

- กำจัดตัวแปรที่มีข้อมูลไม่เพียงพอ
- จัดการข้อมูลที่ขาดหายเพื่อให้โมเดลสามารถเรียนรู้ได้อย่างมีประสิทธิภาพ

ขั้นตอนนี้ช่วยลด Bias และเพิ่มความน่าเชื่อถือของผลลัพธ์

---

## 3. Feature Engineering

เพื่อเพิ่มคุณค่าทางคลินิกของข้อมูล ทีมงานได้ดำเนินการสร้างตัวแปรเพิ่มเติมจากข้อมูลดิบ

### Clinical Score Construction

สร้างตัวแปร clinical_score เพื่อสะท้อนสถานะการฟื้นตัวโดยรวมของผู้ป่วย

### Recovery-Oriented Features

ออกแบบตัวแปรที่ช่วยสะท้อนการเปลี่ยนแปลงของระบบเผาผลาญที่เกี่ยวข้องกับการฟื้นตัว

### Biomarker Integration

รวมข้อมูลจาก Biomarkers หลายตัวเพื่อสร้างตัวแปรที่มีความหมายทางชีวภาพมากขึ้น

ผลลัพธ์คือชุดตัวแปรที่สามารถสะท้อนสภาวะทางคลินิกได้ดีกว่าการใช้ค่าดิบเพียงอย่างเดียว

---

## 4. Data Standardization

เนื่องจาก Biomarkers แต่ละชนิดมีช่วงค่าที่แตกต่างกันอย่างมาก

ตัวอย่างเช่น

- Amino Acids
- Organic Acids
- Ketone Bodies

จึงจำเป็นต้องปรับมาตรฐานข้อมูลก่อนการฝึกโมเดล

### Standardization Objectives

- ลดผลกระทบจากหน่วยวัดที่แตกต่างกัน
- เพิ่มเสถียรภาพของโมเดล
- ป้องกันตัวแปรที่มีค่าสูงครอบงำตัวแปรอื่น

ขั้นตอนนี้ช่วยให้ Biomarkers ทุกตัวมีโอกาสถูกประเมินอย่างเป็นธรรม

---

## 5. Multi-Stage Feature Selection

เนื่องจากข้อมูล Metabolomics ประกอบด้วย Biomarkers จำนวนมาก การใช้ทุกตัวแปรอาจทำให้โมเดลเกิด Overfitting และลดความสามารถในการอธิบายผลลัพธ์

ทีมงานจึงพัฒนา Feature Selection Pipeline หลายขั้นตอน

### Stage 1: Feature Importance Analysis

ประเมินความสำคัญของ Biomarkers ด้วย Machine Learning

วัตถุประสงค์

- ระบุ Biomarkers ที่มีผลต่อ Outcome
- ตัดตัวแปรที่มีผลกระทบต่ำ

---

### Stage 2: Boruta Feature Selection

ใช้ Boruta Algorithm เพื่อคัดเลือก Biomarkers ที่มีความสำคัญอย่างมีนัยสำคัญ

ข้อดี

- ลด Noise
- เพิ่มความเสถียรของโมเดล
- คงไว้เฉพาะตัวแปรที่มีคุณค่าจริง

---

### Stage 3: Recursive Feature Evaluation

ประเมินผลของแต่ละ Biomarker แบบลำดับขั้น

วิเคราะห์ว่า

- ตัวแปรใดควรเก็บไว้
- ตัวแปรใดสามารถตัดออกได้

---

### Stage 4: Leave-One-Feature-Out Analysis

ทดสอบโดยนำ Biomarker ออกทีละตัว

เพื่อประเมินว่า

Biomarker นั้นมีผลต่อ Accuracy มากน้อยเพียงใด

ช่วยระบุ Biomarkers ที่มีความสำคัญเชิงคลินิกสูง

---

### Stage 5: Exhaustive Feature Search

ทดลองชุด Biomarkers หลายรูปแบบ

เพื่อค้นหาชุดตัวแปรที่ให้ประสิทธิภาพสูงสุด

วัตถุประสงค์

- ลดจำนวนตัวแปร
- เพิ่ม Accuracy
- ลด Overfitting

---

## 6. Final Biomarker Selection

หลังจากผ่านกระบวนการ Feature Selection หลายขั้นตอน ทีมงานได้คัดเลือก Biomarkers สำคัญจำนวน 7 ตัวสำหรับ Champion Model

ประกอบด้วย

1. clinical_score
2. glycine_preop
3. L-glutamine_3m
4. L-allo-Isoleucine_3m
5. creatinine_preop
6. L-valine_preop
7. (R)-3-Hydroxybutyric acid_3m

Biomarkers เหล่านี้ถูกใช้เป็นตัวแปรหลักในการสร้างโมเดลทำนายผลการฟื้นตัวและการวิเคราะห์ Biomarker Patterns ในขั้นตอนถัดไป

7. Champion Model Preparation

ชุดข้อมูลที่ผ่านการคัดเลือกแล้วจะถูกนำเข้าสู่กระบวนการพัฒนา Champion Model

โดยใช้

* Optimized Random Forest
* Cross Validation
* Hyperparameter Optimization
* Explainable AI Analysis

# Champion Model Development

การพัฒนา Champion Model เป็นหัวใจสำคัญของโครงการ MetaboRecovery AI โดยทีมงานมุ่งเน้นการสร้างโมเดลที่ไม่เพียงมีความแม่นยำสูง แต่ยังสามารถอธิบายผลลัพธ์ในเชิงคลินิกได้อย่างโปร่งใส เพื่อให้สามารถนำไปใช้เป็นระบบสนับสนุนการตัดสินใจทางการแพทย์ได้ในอนาคต

แทนที่จะเลือกใช้โมเดลเพียงรูปแบบเดียว ทีมงานได้ดำเนินการพัฒนาและเปรียบเทียบ Machine Learning Pipelines หลายรูปแบบอย่างเป็นระบบ เพื่อค้นหาโมเดลที่เหมาะสมที่สุดสำหรับข้อมูล Metabolomics และโจทย์การทำนายผลการฟื้นตัวของผู้ป่วย

---

## Research and Development Strategy

แนวทางการพัฒนาโมเดลแบ่งออกเป็นหลายระยะ โดยแต่ละระยะมีวัตถุประสงค์เฉพาะ

### Phase 1: Baseline Performance Assessment

ในระยะแรก ทีมงานสร้าง Baseline Models เพื่อประเมินศักยภาพของชุดข้อมูล

วัตถุประสงค์

- ตรวจสอบว่าข้อมูล Metabolomics สามารถแยกกลุ่ม Fast Recovery และ Poor Recovery ได้หรือไม่
- ศึกษาพฤติกรรมของ Biomarkers ต่อ Outcome
- สร้างค่าอ้างอิงสำหรับการพัฒนาโมเดลขั้นสูง

ผลลัพธ์จากระยะนี้ยืนยันว่าชุดข้อมูลมีศักยภาพเพียงพอสำหรับการพัฒนา Predictive Model

---

### Phase 2: Biomarker Optimization

เนื่องจากข้อมูล Metabolomics ประกอบด้วย Biomarkers จำนวนมาก การใช้ทุกตัวแปรพร้อมกันอาจทำให้โมเดลเกิด Overfitting และลดความสามารถในการตีความผลลัพธ์

ทีมจึงพัฒนา Biomarker Selection Pipeline แบบหลายชั้น

ประกอบด้วย

- Feature Importance Analysis
- Boruta Feature Selection
- Recursive Feature Evaluation
- Leave-One-Feature-Out Analysis
- Exhaustive Feature Search

เป้าหมายคือ

- ลดจำนวนตัวแปรที่ไม่จำเป็น
- เพิ่มความสามารถในการ Generalize
- ค้นหา Biomarkers ที่มีความหมายทางคลินิก

หลังจากกระบวนการคัดเลือกหลายรอบ ทีมงานสามารถลดจำนวน Biomarkers ลงเหลือชุดที่มีประสิทธิภาพสูงสุด

---

### Phase 3: Model Architecture Exploration

ทีมงานได้ทดลอง Machine Learning Pipelines หลายรูปแบบ

รวมถึง

- Baseline Models
- Random Forest Variants
- Tuned Random Forest Models
- Ensemble-Based Approaches
- Feature Selection Pipelines

แต่ละ Pipeline ถูกออกแบบให้แตกต่างกันในด้าน

- จำนวน Biomarkers
- Hyperparameters
- Selection Strategy
- Model Complexity

เพื่อค้นหาโครงสร้างที่เหมาะสมที่สุดสำหรับข้อมูลชุดนี้

---

### Phase 4: Hyperparameter Optimization

หลังจากได้ Candidate Models หลายเวอร์ชัน ทีมงานได้ดำเนินการปรับแต่ง Hyperparameters อย่างเป็นระบบ

ตัวอย่างพารามิเตอร์ที่ถูกปรับปรุง

- Number of Trees
- Maximum Tree Depth
- Minimum Samples Split
- Minimum Samples Leaf
- Random Seed Configuration

วัตถุประสงค์

- เพิ่ม Accuracy
- ลด Variance
- ลด Overfitting
- เพิ่มเสถียรภาพของโมเดล

---

### Phase 5: Champion Candidate Selection

หลังจากการทดลองหลายรอบ ทีมงานได้สร้าง Candidate Models หลายเวอร์ชัน

แต่ละ Candidate ถูกเปรียบเทียบโดยใช้เกณฑ์เดียวกัน

ได้แก่

- Accuracy
- Cross Validation Stability
- Interpretability
- Clinical Relevance
- Computational Efficiency

โมเดลที่ผ่านเกณฑ์สูงสุดจะถูกนำเข้าสู่กระบวนการ Champion Selection

---

## Model Evaluation Framework

เพื่อให้ผลลัพธ์มีความน่าเชื่อถือ ทีมงานใช้ Stratified 5-Fold Cross Validation เป็นมาตรฐานในการประเมินทุกโมเดล

กระบวนการประกอบด้วย

1. แบ่งข้อมูลออกเป็น 5 ส่วน
2. ใช้ 4 ส่วนสำหรับฝึกโมเดล
3. ใช้ 1 ส่วนสำหรับทดสอบ
4. ทำซ้ำจนครบทุก Fold
5. คำนวณค่าเฉลี่ยของผลลัพธ์ทั้งหมด

ข้อดีของแนวทางนี้

- ลด Bias จากการแบ่งข้อมูลเพียงครั้งเดียว
- ลดความผันผวนของผลลัพธ์
- ประเมินความสามารถในการ Generalize ได้ดีกว่า Train-Test Split แบบทั่วไป

---

## Official Champion Model

หลังจากผ่านกระบวนการคัดเลือกหลายรอบ ทีมงานได้คัดเลือก Official Champion Model ซึ่งเป็นโมเดลที่มีสมดุลดีที่สุดระหว่างความแม่นยำ ความเสถียร และความสามารถในการอธิบายผลลัพธ์

Champion Model ประกอบด้วย

### Optimized Random Forest Engine

ใช้ Random Forest ที่ผ่านการปรับแต่ง Hyperparameters เพื่อให้เหมาะสมกับข้อมูล Metabolomics

### Biomarker Selection Layer

ใช้เฉพาะ Biomarkers ที่ผ่านกระบวนการคัดเลือกและพิสูจน์แล้วว่ามีความสำคัญต่อ Outcome

### Explainable AI Layer

วิเคราะห์ Feature Importance และ Biomarker Contributions เพื่ออธิบายเหตุผลของการทำนาย

### Clinical Interpretation Layer

แปลงผลลัพธ์ของโมเดลให้เป็นข้อมูลที่บุคลากรทางการแพทย์สามารถเข้าใจได้

---

## Selected Biomarkers

Biomarkers ที่ได้รับการคัดเลือกเข้าสู่ Champion Model ได้แก่

1. clinical_score
2. glycine_preop
3. L-glutamine_3m
4. L-allo-Isoleucine_3m
5. creatinine_preop
6. L-valine_preop
7. (R)-3-Hydroxybutyric acid_3m

Biomarkers เหล่านี้แสดงศักยภาพสูงในการจำแนกผู้ป่วยที่มีแนวโน้มฟื้นตัวเร็วและฟื้นตัวช้า

---

## Model Performance

ผลการประเมิน Official Champion Model

Validation Method

Stratified 5-Fold Cross Validation

Cross Validation Scores

- 0.90
- 0.90
- 0.89
- 1.00
- 0.89

Average Cross Validation Accuracy

91.56%

Training Accuracy

97.87%

ผลลัพธ์แสดงให้เห็นว่าโมเดลสามารถเรียนรู้รูปแบบของข้อมูลได้อย่างมีประสิทธิภาพ พร้อมทั้งรักษาความสามารถในการทำนายกับข้อมูลที่ไม่เคยเห็นมาก่อน

---

## Beyond Prediction: Clinical Intelligence Layer

จุดเด่นสำคัญของ Champion Model คือการไม่ได้หยุดอยู่เพียงการทำนายผลการฟื้นตัว

ระบบสามารถนำ Biomarkers ที่ค้นพบมาวิเคราะห์ต่อในระดับ Clinical Intellige

ประกอบด้วย

* Biomarker Contribution Analysis
* Metabolic Alert Detection
* Risk Assessment
* Clinical Interpretation
* Metabolic Pattern Analysis

ตัวอย่างรูปแบบที่สามารถตรวจพบได้

Strong Association

* Insulin Resistance Pattern
* Metabolic Syndrome Risk

Moderate Association

* Diabetes-like Metabolic Signature
* Hypertension-associated Metabolic Pattern

แนวทางดังกล่าวช่วยเปลี่ยนผลลัพธ์ของโมเดลจากการเป็นเพียง Prediction Tool ไปสู่ Clinical Decision Support Platform ที่สามารถสนับสนุนการตีความเชิงคลินิกและการวิจัยด้าน Biomarker Discovery ได้ในอนาคต
---

# Biomarker Discovery Results

Biomarkers สำคัญที่ระบบค้นพบ

1. clinical_score (37.4%)
2. glycine_preop (17.5%)
3. L-glutamine_3m (11.0%)
4. L-allo-Isoleucine_3m (10.5%)
5. creatinine_preop (10.5%)
6. L-valine_preop (7.9%)
7. (R)-3-Hydroxybutyric acid_3m (5.2%)

Biomarkers เหล่านี้เป็นปัจจัยสำคัญที่ส่งผลต่อการทำนายผลการฟื้นตัวของผู้ป่วย

---

# Explainable AI

ระบบสามารถอธิบายผลการตัดสินใจของโมเดลได้ผ่าน

- Feature Importance Ranking
- Biomarker Contribution Analysis
- Biomarker Deviation Analysis
- Clinical Interpretation Layer
- Risk Assessment

ช่วยให้บุคลากรทางการแพทย์เข้าใจเหตุผลของการทำนายได้อย่างโปร่งใส

---

# Metabolic Pattern Analysis

นอกจากการทำนาย Recovery Outcome แล้ว ระบบยังสามารถวิเคราะห์รูปแบบทางเมตาบอลิซึมจาก Biomarkers ที่ตรวจพบ

ตัวอย่างรูปแบบที่สามารถระบุได้

Strong Association

- Insulin Resistance Pattern
- Metabolic Syndrome Risk

Moderate Association

- Diabetes-like Metabolic Signature
- Hypertension-associated Metabolic Pattern

ผลลัพธ์ส่วนนี้ใช้เพื่อสนับสนุนการตีความเชิงคลินิกและการวิจัยด้าน Biomarker Discovery

หมายเหตุ

ระบบไม่ได้ใช้สำหรับการวินิจฉัยโรคโดยตรง แต่ใช้เพื่อระบุความคล้ายคลึงของ Biomarker Patterns ที่รายงานในวรรณกรรมทางการแพทย์

---

# Clinical AI Report

ระบบสามารถสร้างรายงานอัตโนมัติสำหรับผู้ป่วยแต่ละราย ประกอบด้วย

- Prediction Result
- Confidence Score
- Key Clinical Drivers
- Metabolic Alerts
- Clinical Interpretation
- Clinical Risk Summary
- Final Assessment
- Metabolic Pattern Analysis

---

# Dashboard Prototype

Prototype ถูกพัฒนาในรูปแบบ Clinical AI Dashboard

ประกอบด้วย

- Recovery Outcome Prediction
- Model Performance Monitoring
- Biomarker Importance Visualization
- Recovery Distribution
- PCA Recovery Clusters
- Explainable AI Analysis
- Clinical Report Viewer
- Metabolic Pattern Analysis

---

# Innovation

จุดเด่นของโครงการ

1. ใช้ข้อมูล Metabolomics เพื่อทำนายผลการฟื้นตัวของผู้ป่วย
2. ค้นหา Biomarkers สำคัญด้วย Machine Learning
3. ผสาน Explainable AI เข้ากับ Clinical Reporting
4. วิเคราะห์ Metabolic Patterns เพิ่มเติมจาก Biomarker Signatures
5. สร้าง Clinical Decision Support Dashboard สำหรับการใช้งานจริง

---

# Expected Impact

- ช่วยสนับสนุนการประเมินความเสี่ยงของผู้ป่วยหลังการผ่าตัด
- ช่วยค้นหา Biomarkers ที่เกี่ยวข้องกับผลลัพธ์ทางคลินิก
- เพิ่มความโปร่งใสของ AI ในงานทางการแพทย์
-