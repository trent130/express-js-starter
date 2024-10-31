const mongoose = require("mongoose");

const ProductSchema = mongoose.Schema(
  {
    name: {
      type: String,
      required: [true, "Please enter your product name"],
    },
    quantity: {
      type: Number,
      required: [true, "Please enter your product quantity"],
      default: 0,
    },
    price: {
      type: Number,
      required: [true, "Please enter your product price"],
      default: 0,
    },
    image: {
      type: String,
      required: false,
    },
  },
  {
    timestamp: true,
  }
);

const Product = mangoose.model("Product", ProductSchema)
module.exports = Product;