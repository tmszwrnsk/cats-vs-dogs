#include <iostream>
#include <exception>
#include <fdeep/fdeep.hpp>
#include <opencv2/core/core.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>

int main(int argc, char* argv[])
{
    if (argc != 3)
    {
        std::cerr << "usage: cat-vs-dog <Model_Path> <Image_Path>" << std::endl;
        return -1;
    }

    const auto model = fdeep::load_model(argv[1]);

    try
    {
        cv::Mat image = cv::imread(argv[2]);
        cv::Mat resizedImage;
        cv::resize(image, resizedImage, cv::Size(150, 150));

        cv::imshow("Display Image", image);

        // convert cv::Mat to fdeep::tensor
        const auto input = fdeep::tensor_from_bytes(resizedImage.ptr(),
            static_cast<std::size_t>(resizedImage.rows),
            static_cast<std::size_t>(resizedImage.cols),
            static_cast<std::size_t>(resizedImage.channels()),
            0.0f, 1.0f
        );

        auto result = model.predict({ input });
        std::cout << fdeep::show_tensors(result) << std::endl;

        cv::waitKey(0);
    }
    catch(const std::exception& e)
    {
        std::cerr << e.what() << '\n';
        return -1;
    }

    return 0;
}