import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Audio Player',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const AudioPlayer(title: 'Audio Player Demo Home Page'),
    );
  }
}

class AudioPlayer extends StatefulWidget {
  const AudioPlayer({Key? key, required this.title}) : super(key: key);

  final String title;

  @override
  State<AudioPlayer> createState() => _AudioPlayerState();
}

class _AudioPlayerState extends State<AudioPlayer> {
  String playStatus = 'stopped';
  Icon playStatusIcon = const Icon(Icons.play_arrow);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            IconButton(onPressed: () {
              setState(() {
                switch (playStatus) {
                  case 'stopped':
                    playStatus = 'playing';
                    playStatusIcon = const Icon(Icons.stop);
                    break;
                  case 'playing':
                    playStatus = 'stopped';
                    playStatusIcon = const Icon(Icons.play_arrow);
                    break;
                  default:
                    playStatus = 'stopped';
                    playStatusIcon = const Icon(Icons.play_arrow);
                }
              });
            }, icon: playStatusIcon),
          ],
        ),
      ),
    );
  }
}
