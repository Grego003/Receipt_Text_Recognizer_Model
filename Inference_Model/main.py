import os
import argparse
from inference.InferenceModel import InferenceModel


TRAINED_MODEL_DIR = "./trained_models"

YOLO_MODEL_DIR = os.path.join(TRAINED_MODEL_DIR, "YOLO")
YOLO_BEST_MODEL = os.path.join("model_train_renfred_1", "weights", "best.pt")
YOLO_MODEL_PATH = os.path.join(YOLO_MODEL_DIR, YOLO_BEST_MODEL)

OCR_MODEL_DIR = os.path.join(TRAINED_MODEL_DIR, "OCR")
OCR_BEST_MODEL = os.path.join("CRNN_Model_AgusV3", "model", "CRNN_Model_AgusV3.keras")
OCR_BEST_WEIGHTS = os.path.join(
    OCR_MODEL_DIR, "CRNN_Model_augmented", "weight", "best_weight.keras"
)
OCR_MODEL_PATH = os.path.join(OCR_MODEL_DIR, OCR_BEST_MODEL)

SAMPLE_IMAGE_PATH = os.path.join("./sample_image")


def predict(image_path, conf_limit=0.5, use_augment=False):
    model = InferenceModel(YOLO_MODEL_PATH, OCR_BEST_WEIGHTS, conf_limit, use_augment)

    # Run inference on the provided image
    result = model.predict(image_path)

    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Command-line tool for predicting Receipts."
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    predict_parser = subparsers.add_parser("predict", help="Run inference on a receipt")

    predict_parser.add_argument("image_path", type=str, help="Path to the input image")

    predict_parser.add_argument(
        "--conf_limit",
        type=float,
        default=0.5,
        help="Confidence limit for predictions (default: 0.5)",
    )
    predict_parser.add_argument(
        "--use_augment", action="store_true", help="Enable augmentation for inference"
    )

    args = parser.parse_args()

    if args.command == "predict":
        result = predict(args.image_path, args.conf_limit, args.use_augment)
        print(result)
    else:
        parser.print_help()